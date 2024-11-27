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

    else:
        form = FileUploadForm()

    # Handle search queries
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

    # Fetch uploaded files from the database
    uploaded_files = Dataset.objects.filter(user=request.user)

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