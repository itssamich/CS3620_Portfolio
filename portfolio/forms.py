from django import forms
from .models import Project

class projForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['proj_name', 'proj_desc', 'proj_img']
