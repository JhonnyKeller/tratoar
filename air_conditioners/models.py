from django.db import models
from django.contrib import auth
from django.views.generic import TemplateView,CreateView
from django.core.exceptions import ValidationError
from django.conf import settings
from brands.models import AcBrands
from categories.models import Categories,SubCategories
from django.urls import reverse

import misaka

# Create your models here.

class AirConditioner(models.Model):
    brand = models.ForeignKey(AcBrands,related_name='brands',on_delete=models.CASCADE)
    categorie = models.ForeignKey(Categories,related_name='procat',on_delete=models.CASCADE)
    sub_categorie = models.ForeignKey(SubCategories,related_name='prosubcat',on_delete=models.CASCADE)
    title = models.CharField(max_length=254, unique=True)
    energy_efficiency = models.CharField(max_length=254, blank=True)
    btu = models.PositiveIntegerField(blank=True,default='0')
    description = models.TextField()
    ac_img = models.FileField(upload_to='ac_img')


    def get_absolute_url(self):
        return reverse("air_conditioners:ac_createview")
    # saving it just in case i need to use the detailview
# , kwargs={'pk':self.pk}

    def __str__(self):
        return self.title
