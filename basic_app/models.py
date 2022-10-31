from django.db import models
from django.contrib import auth
from django.views.generic import TemplateView,CreateView
from django.core.exceptions import ValidationError
from django.conf import settings
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
# pip install misaka
import misaka

from django.template.defaultfilters import slugify
import os

from django.contrib.auth import get_user_model
User = get_user_model()




def validate_file_size(value):
    filesize = value.size

    if filesize > 10485760:
        raise ValidationError("You cannot upload file more than 10Mb")
    else:
        return value




class Budget(models.Model):
    HouseDivision = [
    # ('Selecionar Divisão', 'Selecionar Divisão'),
    ('Quarto', 'Quarto'),
    ('Sala', 'Sala'),
    ('Cozinha', 'Cozinha'),
    ('Garagem', 'Garagem'),
    ('Sotão', 'Sotão'),
    ('Outros', 'Outros'),
]
    updated_status = [
    ('Aguarda Orçamento','Aguarda Orçamento'),
    ('Requer-se mais informação','Requer-se mais informação'),
    ('Orçamento enviado','Orçamento enviado'),
    ('Orçamento sem efeito','Orçamento sem efeito'),
    ]

    instalation_type = [
    # ('Tipo de instalação','Tipo de instalação'),
    ('Manutenção','Manutenção'),
    ('Instalação Monosplit','Instalação Monosplit'),
    ('Instalação Multisplit','Instalação Multisplit'),
    ]
    # user = models.ForeignKey(User,related_name='user_budget',on_delete=models.CASCADE)
    status = models.CharField(choices=updated_status,max_length=64,default=updated_status[0][0])
    name = models.CharField(max_length=128,verbose_name='Nome Completo',default='')
    email = models.EmailField(default='')
    phone_number = PhoneNumberField(blank=True,verbose_name='Contact: Exemplo - (+351 969679224)',default='+351')
    zip_code = models.CharField(max_length=64, default="1372-010",verbose_name='Código Postal')
    address = models.CharField(default="Rua e Localidade", max_length=128,verbose_name='Morada')
    created_at = models.DateTimeField(auto_now=True)
    Instalation = models.CharField(choices=instalation_type,max_length=128, verbose_name='Tipo de instalação')
    budget_text = models.TextField(default='Por favor faça uma breve descrição.',verbose_name='Descrição:')
    Division_1 = models.CharField(choices=HouseDivision,max_length=64,verbose_name='Divisão 1')
    Division_2 = models.CharField(choices=HouseDivision,max_length=64,blank=True,verbose_name='Divisão 2')
    Division_3 = models.CharField(choices=HouseDivision,max_length=64,blank=True,verbose_name='Divisão 3')
    Division_4 = models.CharField(choices=HouseDivision,max_length=64,blank=True,verbose_name='Divisão 4')
    Division_5 = models.CharField(choices=HouseDivision,max_length=64,blank=True,verbose_name='Divisão 5')
    Division_6 = models.CharField(choices=HouseDivision,max_length=64,blank=True,verbose_name='Divisão 6')
    Area_1 = models.PositiveIntegerField()
    Area_2 = models.PositiveIntegerField(blank=True,default='0')
    Area_3 = models.PositiveIntegerField(blank=True,default='0')
    Area_4 = models.PositiveIntegerField(blank=True,default='0')
    Area_5 = models.PositiveIntegerField(blank=True,default='0')
    Area_6 = models.PositiveIntegerField(blank=True,default='0')
    File_1 = models.FileField(upload_to='examples',blank=True)
    File_2 = models.FileField(upload_to='examples',blank=True)
    File_3 = models.FileField(upload_to='examples',blank=True)
    File_4 = models.FileField(upload_to='examples',blank=True)
    File_5 = models.FileField(upload_to='examples',blank=True)

    def __str__(self):
        return self.zip_code

    def get_absolute_url(self):
        return reverse('basic_app:user_budget_list', kwargs={'username':self.user.username})
        #     "posts:single",
        #     kwargs={
        #         "username": self.user.username,
        #         "pk": self.pk
        #     }
        # )
    def clean_file_size(self):
        file_1 = self.cleaned_data.get('File_1')

        validate_file_size(file_1)

        return file_1
