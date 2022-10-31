from django.db import models
from django.contrib import auth
from django.views.generic import TemplateView,CreateView
from django.core.exceptions import ValidationError
from django.conf import settings
from django.urls import reverse

import misaka

# Create your models here.

class Categories(models.Model):
    title = models.CharField(max_length=254, unique=True)


    def get_absolute_url(self):
        return reverse("categories:cg_createview")


    def __str__(self):
        return self.title

class SubCategories(models.Model):
    Categorie = models.ForeignKey(Categories,related_name='subcats',on_delete=models.CASCADE)
    title = models.CharField(max_length=254, unique=True)


    def get_absolute_url(self):
        return reverse("categories:subcat_createview")


    def __str__(self):
        return self.title
