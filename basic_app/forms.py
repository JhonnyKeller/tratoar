from django import forms
from django.forms import ModelForm
from .models import Budget
from captcha.fields import ReCaptchaField

class  BudgetForm(ModelForm):
    captcha = ReCaptchaField()
    class Meta:
        model = Budget
        fields = ['zip_code','address','phone_number','name','email','Instalation','budget_text','Division_1','Division_2',
                 'Division_3','Division_4','Division_5','Division_6','Area_1',
                 'Area_2','Area_3','Area_4','Area_5','Area_6','File_1','File_2',
                 'File_3','File_4','File_5','captcha']

class contactForm(forms.Form):
    name = forms.CharField(label='Nome', max_length='100')
    Email = forms.EmailField(label='Email', max_length='100')
    phone_number = forms.CharField(label='Telemóvel', max_length='100', required=False)
    subject = forms.CharField(label='Assunto', max_length='100')
    message = forms.CharField(label='Mensagem')
    captcha = ReCaptchaField()
