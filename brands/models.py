from django.db import models
from django.urls import reverse

# Create your models here.
class AcBrands(models.Model):
    title = models.CharField(max_length=254,unique=True)
    brand_url = models.URLField(max_length=200)
    brand_img = models.FileField(upload_to='brand_img')


    def get_absolute_url(self):
        return reverse('brands:brand_detailview', kwargs={'pk':self.pk})


    def __str__(self):
        return self.title
