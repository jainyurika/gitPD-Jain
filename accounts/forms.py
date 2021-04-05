from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Account
from django.contrib.admin.widgets import AdminDateWidget
from django.conf import settings

class DateInput(forms.DateInput):
    input_type = 'date'

class SignUpForm(UserCreationForm):
    EXPERIENCE_OPTIONS = [
        ('Beginner', 'Beginner'),
        ('Amateur', 'Amateur'),
        ('Semi-Pro', 'Semi-Pro'),
        ('Professional', 'Professional'),
    ]
    # input_formats=settings.DATE_INPUT_FORMATS

    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirm Password'}))
    dob = forms.DateField(input_formats=settings.DATE_INPUT_FORMATS, required=False,widget=DateInput(attrs={'class': 'form-control', 'placeholder': 'Date of Birth'}))
    experience = forms.ChoiceField(choices=EXPERIENCE_OPTIONS, required=True, widget=forms.Select(attrs={'class':'form-control'}))
    
    class Meta(UserCreationForm.Meta):
        model = Account
        fields = ['username', 'email', 'dob', 'experience', 'phone', 'password1', 'password2']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}),    
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone'}),    
            }