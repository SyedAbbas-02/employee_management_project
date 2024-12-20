from django import forms
from .models import Employee
from django.contrib.auth.forms import AuthenticationForm
import re

class LoginForm(forms.Form):
    username = forms.CharField(
        label='User Name',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Username'
        })
    )
    password = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Password',
            'id': 'id_password'
        })
    )

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['name', 'email', 'mobile', 'designation', 'gender', 'course', 'image']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'mobile': forms.TextInput(attrs={'class': 'form-control'}),
            'designation': forms.Select(attrs={'class': 'form-control'}),
            'gender': forms.RadioSelect(attrs={'class': 'form-check-input'}),
            'course': forms.Select(attrs={'class': 'form-control'}),
            'image': forms.FileInput(attrs={'class': 'form-control'})
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        instance = kwargs.get('instance')
        if instance:
            self.fields['gender'].initial = instance.gender
            self.fields['course'].initial = instance.course

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if self.instance.pk:  # If this is an existing employee (edit mode)
            # Exclude the current instance from the uniqueness check
            exists = Employee.objects.filter(email=email).exclude(pk=self.instance.pk).exists()
        else:  # If this is a new employee
            exists = Employee.objects.filter(email=email).exists()
            
        if exists:
            raise forms.ValidationError('This email is already registered')
        return email

    def clean_mobile(self):
        mobile = self.cleaned_data.get('mobile')
        if not re.match(r'^\d{10}$', mobile):
            raise forms.ValidationError('Mobile number must be 10 digits')
        return mobile

    def clean_image(self):
        image = self.cleaned_data.get('image')
        if image:
            ext = image.name.split('.')[-1].lower()
            if ext not in ['jpg', 'jpeg', 'png']:
                raise forms.ValidationError('Only JPG and PNG files are allowed')
        return image 