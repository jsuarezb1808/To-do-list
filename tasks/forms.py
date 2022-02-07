from django import forms
from .import models

class CreateTask(forms.ModelForm):
    class Meta:
        model=models.task
        fields=['title','slug','content','status']
