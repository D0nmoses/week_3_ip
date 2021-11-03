from django import forms
from .models import Project


class NewPostForm(forms.ModelForm):
    '''	
    Class to create a form for an authenticated user to create Post	
    '''
    class Meta:
        model = Project
        exclude = ['user','profile']
