# -*- coding:utf-8 -*-
from django import forms

class ImageUploadForm(forms.Form):
    """Image upload form."""
    image = forms.FileField()
    
class SearchForm(forms.Form):
    Search = forms.CharField(min_length=1,max_length=10)
    
class ModifyForm(forms.Form):
    title = forms.CharField(min_length=1,max_length=20)
