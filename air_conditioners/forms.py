from django import forms
from .models import AirConditioner

class AirConditionerForm(forms.ModelForm):
    class Meta:
        model = AirConditioner
        fields = ('brand','title','categorie','sub_categorie','energy_efficiency','btu','description','ac_img')
