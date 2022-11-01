from pyexpat import model
from django import forms
from .models import Project
# class ProjectForms(forms.Form):
#     first_name = forms.CharField(max_length=100)
#     last_name = forms.CharField(max_length=100)
#     roll = forms.CharField(max_length=100)


class ProjectForms(forms.ModelForm):
    class Meta:
        model=Project
        # field = ['name', 'TechStack']
        fields= '__all__'