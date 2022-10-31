from django import forms
from django.forms import ModelForm
from .models import AcBrands


class AcBrandsForm(ModelForm):
    class Meta:
        model = AcBrands
        fields = ['title','brand_url','brand_img']
