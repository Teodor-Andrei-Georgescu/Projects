from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError

'''
Custom user registration from based on the default django form.

It has some different help text and ensure user username and email.
'''
class UserRegistrationForm(UserCreationForm):
    username = forms.CharField(
        max_length=150,
        required=True,
        help_text="Enter a unique username. Required. 150 characters or fewer. Letters, digits, and @/./+/-/_ only. (Required)"
    )
    first_name = forms.CharField(
        max_length=30, 
        required=True, 
        help_text="Enter your first name. (Required)")
    
    last_name = forms.CharField(
        max_length=30, required=True, 
        help_text="Enter your last name. (Required)"
        )
    email = forms.EmailField(
        max_length=254, 
        required=True, 
        help_text="Enter a valid email address. (Required)"
        )

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise ValidationError("This email address is already in use.")
        return email
    
    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            raise ValidationError("This username  is already in use.")
        return username

'''
Simple form to file uploading.
'''
class FileUploadForm(forms.Form):
    file = forms.FileField(label="Select a file")