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


from django.core.paginator import Paginator

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

    # Fetch the logged-in user's uploaded files, ordered by the most recent
    uploaded_files = Dataset.objects.filter(user=request.user).order_by('-upload_date')

    # Search functionality
    search_query = request.GET.get('search', '')
    if search_query:
        uploaded_files = uploaded_files.filter(filename__icontains=search_query)

    # Paginate the files, 10 files per page
    paginator = Paginator(uploaded_files, 10)  # Show 10 files per page
    page_number = request.GET.get('page')  # Get the current page number from the query parameters
    page_obj = paginator.get_page(page_number)  # Get the files for the current page

    return render(request, 'file_upload.html', {
        'form': form,
        'page_obj': page_obj,  # Pass the paginated files
        'search_query': search_query,  # Pass the current search query for reuse in the template
    })
