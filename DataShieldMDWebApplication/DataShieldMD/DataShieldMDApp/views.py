from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from .forms import *
from .models import *
from django.contrib.messages import get_messages

import os
from django.conf import settings
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from datetime import datetime


'''
Home page, only displays info.
'''
def home(request):
    return render(request, 'home.html')


'''
How we do it page, only displays info.
'''
def how_we_do_it(request):
    return render(request, 'how_we_do_it.html')

'''
Registration page, handles user registrion and displays errors to users if neeed.
Otherwise just saves the from and submits info to databse.
'''
def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registration successful! You can now log in.')
            return redirect('login')
        else:
            messages.error(request, 'Registration failed. Please check the form.')
    else:
        form = UserRegistrationForm()
    return render(request, 'register.html', {'form': form})

'''
Login page, handles usser log in and displays errors to users if neeed.
Otherwise just logs user in.
'''
def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, f"Welcome {user.username}!")
            return redirect('home')  # Ensure this route exists
        else:
            messages.error(request, 'Invalid username or password.')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

'''
When user presses the logout button they get signed out and returned to home page.
'''
def user_logout(request):
    logout(request)
    messages.success(request, 'Logged out successfully.')
    return redirect('home')


@login_required
def upload_file(request):
    if request.method == 'POST':
        # Handle file upload
        if 'file' in request.FILES:
            form = FileUploadForm(request.POST, request.FILES)
            if form.is_valid():
                file = form.cleaned_data['file']

                # Define the user's upload directory
                user_dir = os.path.join(settings.MEDIA_ROOT, request.user.username, 'uploads')
                os.makedirs(user_dir, exist_ok=True)

                # Save the file to the user's upload directory
                file_path = os.path.join(user_dir, file.name)
                with open(file_path, 'wb+') as destination:
                    for chunk in file.chunks():
                        destination.write(chunk)

                # Save file information to the Dataset model
                Dataset.objects.create(
                    user=request.user,
                    filename=file.name,
                    file_path=file_path
                )
                return redirect('upload_file')  # Refresh the page

        # Handle file deletion
        if 'delete_file' in request.POST:
            file_to_delete = request.POST.get('delete_file')
            user_dir = os.path.join(settings.MEDIA_ROOT, request.user.username, 'uploads')
            file_path = os.path.join(user_dir, file_to_delete)

            if os.path.exists(file_path):
                os.remove(file_path)  # Delete the file from the directory

            return redirect('upload_file')  # Refresh the page

    else:
        form = FileUploadForm()

    # Handle search queries and view mode
    search_query = request.GET.get('search', '')
    search_date = request.GET.get('search_date', '')
    view_mode = request.GET.get('view_mode', '')

    if view_mode == 'current':
        # Fetch current files stored in media/<username>/uploads
        current_files = []
        user_dir = os.path.join(settings.MEDIA_ROOT, request.user.username, 'uploads')
        if os.path.exists(user_dir):
            for file_name in os.listdir(user_dir):
                full_path = os.path.join(user_dir, file_name)
                if os.path.isfile(full_path):
                    file_data = {
                        'filename': file_name,
                        'upload_date': datetime.fromtimestamp(os.path.getmtime(full_path))  # Get file modification time
                    }
                    # Apply search filters
                    if search_query and search_query.lower() not in file_name.lower():
                        continue
                    if search_date:
                        try:
                            search_date_obj = datetime.strptime(search_date, '%Y-%m-%d').date()
                            file_date = datetime.fromtimestamp(os.path.getmtime(full_path)).date()
                            if file_date != search_date_obj:
                                continue
                        except ValueError:
                            pass  # Ignore invalid date inputs
                    current_files.append(file_data)

        # Sort current files by modification date (most recent first)
        current_files = sorted(current_files, key=lambda x: x['upload_date'], reverse=True)

        # Paginate current files
        paginator = Paginator(current_files, 10)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        return render(request, 'file_upload.html', {
            'form': form,
            'page_obj': page_obj,
            'search_query': search_query,
            'search_date': search_date,
            'view_mode': view_mode,
        })

    # Fetch uploaded files from the database and sort by the most recent upload date
    uploaded_files = Dataset.objects.filter(user=request.user).order_by('-upload_date')

    # Apply search filters
    if search_query:
        uploaded_files = uploaded_files.filter(filename__icontains=search_query)

    if search_date:
        try:
            # Parse the date and filter files uploaded on that date
            search_date_obj = datetime.strptime(search_date, '%Y-%m-%d')
            uploaded_files = uploaded_files.filter(upload_date__date=search_date_obj.date())
        except ValueError:
            pass  # Ignore invalid date inputs

    # Paginate uploaded files
    paginator = Paginator(uploaded_files, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'file_upload.html', {
        'form': form,
        'page_obj': page_obj,
        'search_query': search_query,
        'search_date': search_date,
        'view_mode': view_mode,
    })


@login_required
def algorithm_selection(request):
    # Fetch the current user's uploaded files from the directory
    user_dir = os.path.join(settings.MEDIA_ROOT, request.user.username, 'uploads')
    file_choices = [(f, f) for f in os.listdir(user_dir) if os.path.isfile(os.path.join(user_dir, f))] if os.path.exists(user_dir) else []

    if request.method == 'POST':
        form = AlgorithmSelectionForm(request.POST, file_choices=file_choices)
        if form.is_valid():
            # Process the form data
            selected_file = form.cleaned_data['file']
            sensitive_fields = form.cleaned_data['sensitive_fields']
            identifying_fields = form.cleaned_data['identifying_fields']

            # Collect algorithm types and their parameters
            algorithm_type = ""
            k_value = form.cleaned_data.get('k_value')
            l_value = form.cleaned_data.get('l_value')
            t_value = form.cleaned_data.get('t_value')

            if form.cleaned_data.get('k_anonymity'):
                algorithm_type += "K"
            if form.cleaned_data.get('l_diversity'):
                algorithm_type += "L"
            if form.cleaned_data.get('t_closeness'):
                algorithm_type += "T"

            # Validate dataset association
            dataset = Dataset.objects.filter(user=request.user, filename=selected_file).first()
            if not dataset:
                messages.error(request, "Selected file is not associated with any dataset entry.")
                return render(request, 'algorithm_selection_and_processing.html', {'form': form})

            # Save parameters to the database
            AlgorithmParameter.objects.create(
                dataset=dataset,
                algorithm_type=algorithm_type,
                k_value=k_value,
                l_value=l_value,
                t_value=t_value
            )

            # Provide success feedback
            messages.success(request, f"Algorithm parameters saved for {selected_file}!")
            return redirect('algorithm_selection')  # Redirect to clear the form
        else:
            messages.error(request, 'There is some error with your form. Please double check it.')
    else:
        form = AlgorithmSelectionForm(file_choices=file_choices)

    return render(request, 'algorithm_selection.html', {'form': form})
