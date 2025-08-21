from django import forms
from .models import Task
from django.utils import timezone
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("This email address is already registered.")
        return email

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = '__all__'
        widgets = {
            'deadline': forms.DateInput(
                attrs={
                    'type': 'date',  # This triggers the calendar picker
                }
            )
        }
        

    def clean_deadline(self):
        deadline = self.cleaned_data.get('deadline')
        if deadline < timezone.now().date():
            raise forms.ValidationError("Deadline cannot be in the past.")
        return deadline