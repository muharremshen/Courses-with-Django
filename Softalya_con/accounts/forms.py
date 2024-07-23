from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Username',
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Password',
    }))

class RegisterForm(UserCreationForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'First Name',
    }))
    last_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Last Name',
    }))
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Username',
    }))
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class': 'form-control',
        'placeholder': 'Email',
    }))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Password',
    }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Confirm Password',
    }))

    class Meta:
        model = User
        fields = ['first_name', 'last_name','username' ,'email', 'password1','password2']


# from django import forms
# from . models import Contact


# class ContactForm(forms.ModelForm):
#     first_name = forms.CharField(widget=forms.TextInput(attrs={
#         'class': 'form-control',
#         'placeholder': 'First Name',
#     }))
#     last_name = forms.CharField(widget=forms.TextInput(attrs={
#         'class': 'form-control',
#         'placeholder': 'Last Name',
#     }))
#     email = forms.EmailField(widget=forms.TextInput(attrs={
#         'class': 'form-control',
#         'placeholder': 'Your Email',
#     }))
#     phone = forms.CharField(widget=forms.TextInput(attrs={
#         'class': 'form-control',
#         'placeholder': 'Your Phone',
#     }))
#     message = forms.CharField(widget=forms.Textarea(attrs={
#         'class': 'form-control',
#         'placeholder': 'Give us more details..',
#     }))


#     class Meta:
#         model = Contact
#         fields = ['first_name', 'last_name', 'email', 'phone', 'message']