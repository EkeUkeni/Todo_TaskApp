from django import forms
from taskapp.models import Task

class TaskForm(forms.ModelForm):

    class Meta:
        model = Task
        # fields = '__all__'
        # exclude = ['user']
        fields = ['title', 'description', 'completed']
