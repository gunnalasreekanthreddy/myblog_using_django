from django import forms
from .models import *

class BlogForm(forms.ModelForm):
    class Meta:
        model = myblog
        fields = ['bimage']
class addblogcategory1(forms.ModelForm):
    class Meta:
        model = category
        fields = ['bcategory']
