from django import forms
from django.forms import ModelForm
from .models import Categories,SubCategories


class CategoriesForm(ModelForm):

    class Meta:
        model = Categories
        fields = ['title']

class SubCategoriesForm(ModelForm):

    class Meta:
        model = SubCategories
        fields = ['Categorie','title']
