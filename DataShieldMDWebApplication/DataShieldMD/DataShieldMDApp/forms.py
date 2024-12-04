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
    file = forms.FileField(required=True,label="Select a file")
    
    def clean_file(self):
        uploaded_file = self.cleaned_data.get('file')
        if uploaded_file:
            # Get the file extension
            extension = uploaded_file.name.split('.')[-1].lower()
            allowed_extensions = ['xlsx', 'csv']
            if extension not in allowed_extensions:
                raise ValidationError("Only .xlsx and .csv file types are allowed.")
        return uploaded_file
    
'''
Algorithm selection form
'''
class AlgorithmSelectionForm(forms.Form):
    file = forms.ChoiceField(label="Select File")
    sensitive_fields = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'e.g., Age or Salary or Disease'}),
        label="Sensitive Field:"
    )

    # Checkboxes and parameter inputs
    k_anonymity = forms.BooleanField(required=False, label="K-Anonymity")
    k_anonymity_k_value = forms.IntegerField(
        required=False,
        widget=forms.NumberInput(attrs={
            'placeholder': 'Enter K value (min 2)',
            'class': 'algorithm-param',
            'data-algo': 'k_anonymity'
        })
    )
    l_diversity = forms.BooleanField(required=False, label="L-Diversity")
    l_diversity_k_value = forms.IntegerField(
        required=False,
        widget=forms.NumberInput(attrs={
            'placeholder': 'Enter L-diversity K value (min 2)',
            'class': 'algorithm-param',
            'data-algo': 'l_diversity'
        })
    )
    l_value = forms.IntegerField(
        required=False,
        widget=forms.NumberInput(attrs={
            'placeholder': 'Enter L value (min 2 max L-diversity k value)',
            'class': 'algorithm-param',
            'data-algo': 'l_diversity'
        })
    )
    t_closeness = forms.BooleanField(required=False, label="T-Closeness")
    t_closeness_k_value = forms.IntegerField(
        required=False,
        widget=forms.NumberInput(attrs={
            'placeholder': 'Enter T-Closeness K value (min 2)',
            'class': 'algorithm-param',
            'data-algo': 't_closeness'
        })
    )
    t_value = forms.FloatField(
        required=False,
        widget=forms.NumberInput(attrs={
            'placeholder': 'Enter T value (0 - 1)',
            'class': 'algorithm-param',
            'data-algo': 't_closeness'
        })
    )

    def __init__(self, *args, **kwargs):
        file_choices = kwargs.pop('file_choices', [])
        super().__init__(*args, **kwargs)
        self.fields['file'].choices = file_choices

    def clean(self):
        cleaned_data = super().clean()

        # Ensure at least one algorithm is selected
        if not (
            cleaned_data.get('k_anonymity')
            or cleaned_data.get('l_diversity')
            or cleaned_data.get('t_closeness')
        ):
            raise forms.ValidationError("Please select at least one anonymization algorithm.")

        # Validate K-Anonymity
        if cleaned_data.get('k_anonymity'):
            k_anonymity_k_value = cleaned_data.get('k_anonymity_k_value')
            if k_anonymity_k_value is None:
                self.add_error('k_anonymity_k_value', "K value is required if K-Anonymity is selected.")
            elif k_anonymity_k_value < 2:
                self.add_error('k_anonymity_k_value', "K value must be at least 2.")

        # Validate L-Diversity
        if cleaned_data.get('l_diversity'):
            l_diversity_k_value = cleaned_data.get('l_diversity_k_value')
            l_value = cleaned_data.get('l_value')

            # Validate l_diversity_k_value
            if l_diversity_k_value is not None:
                if l_diversity_k_value < 2:
                    self.add_error('l_diversity_k_value', "The L-diversity K value must be at least 2.")

            # Validate l_value
            if l_value is None:
                self.add_error('l_value', "L value is required if L-Diversity is selected.")
            elif l_diversity_k_value is not None:
                if l_value < 2 or l_value < l_diversity_k_value:
                    self.add_error('l_value', "L value must be at least 2 and less than or equal to the chosen L-diversity K value.")
            elif l_value < 2:
                self.add_error('l_value', "L value must be at least 2.")
                
                
        # Validate T-Closeness
        if cleaned_data.get('t_closeness'):
            t_closeness_k_value = cleaned_data.get('t_closeness_k_value')
            t_value = cleaned_data.get('t_value')
            
            if t_closeness_k_value is None:
                self.add_error('t_closeness_k_value', "T-closeness K value is required if T-Closeness is selected. Make sure the value is at least 2.")
            elif t_closeness_k_value< 2:
                self.add_error('t_closeness_k_value', "T-closeness K must be at least 2.")
    
            if t_value is None:
                self.add_error('t_value', "T value is required if T-Closeness is selected.")
            elif not (0 <= t_value <= 1):
                self.add_error('t_value', "T value must be between 0 and 1.")

        return cleaned_data
