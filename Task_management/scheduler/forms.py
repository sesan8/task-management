from django import forms
from .models import User, Task

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name', 'email', 'mobile_number', 'password', 'address']

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['name', 'date_and_time', 'assigned_to']
