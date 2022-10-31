# Generated by Django 4.1 on 2022-09-26 18:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Budget',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('Aguarda Orçamento', 'Aguarda Orçamento'), ('Requer-se mais informação', 'Requer-se mais informação'), ('Orçamento enviado', 'Orçamento enviado'), ('Orçamento sem efeito', 'Orçamento sem efeito')], default='Aguarda Orçamento', max_length=64)),
                ('email', models.EmailField(default='0', max_length=254)),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, region=None)),
                ('zip_code', models.CharField(default='1372-010', max_length=8)),
                ('address', models.CharField(default='Rua e Localidade', max_length=128)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('Instalation', models.BooleanField()),
                ('Fixing', models.BooleanField()),
                ('budget_text', models.TextField(default='Por favor faça uma breve descrição.')),
                ('Division_1', models.CharField(choices=[('A', 'Quarto'), ('B', 'Sala'), ('C', 'Cozinha'), ('D', 'Garagem'), ('E', 'Sotão'), ('F', 'Outros')], default='A', max_length=7)),
                ('Division_2', models.CharField(blank=True, choices=[('A', 'Quarto'), ('B', 'Sala'), ('C', 'Cozinha'), ('D', 'Garagem'), ('E', 'Sotão'), ('F', 'Outros')], default='A', max_length=7)),
                ('Division_3', models.CharField(blank=True, choices=[('A', 'Quarto'), ('B', 'Sala'), ('C', 'Cozinha'), ('D', 'Garagem'), ('E', 'Sotão'), ('F', 'Outros')], default='A', max_length=7)),
                ('Division_4', models.CharField(blank=True, choices=[('A', 'Quarto'), ('B', 'Sala'), ('C', 'Cozinha'), ('D', 'Garagem'), ('E', 'Sotão'), ('F', 'Outros')], default='A', max_length=7)),
                ('Division_5', models.CharField(blank=True, choices=[('A', 'Quarto'), ('B', 'Sala'), ('C', 'Cozinha'), ('D', 'Garagem'), ('E', 'Sotão'), ('F', 'Outros')], default='A', max_length=7)),
                ('Division_6', models.CharField(blank=True, choices=[('A', 'Quarto'), ('B', 'Sala'), ('C', 'Cozinha'), ('D', 'Garagem'), ('E', 'Sotão'), ('F', 'Outros')], default='A', max_length=7)),
                ('Area_1', models.PositiveIntegerField()),
                ('Area_2', models.PositiveIntegerField(blank=True)),
                ('Area_3', models.PositiveIntegerField(blank=True, default='0')),
                ('Area_4', models.PositiveIntegerField(blank=True, default='0')),
                ('Area_5', models.PositiveIntegerField(blank=True, default='0')),
                ('Area_6', models.PositiveIntegerField(blank=True, default='0')),
                ('File_1', models.FileField(blank=True, upload_to='examples')),
                ('File_2', models.FileField(blank=True, upload_to='examples')),
                ('File_3', models.FileField(blank=True, upload_to='examples')),
                ('File_4', models.FileField(blank=True, upload_to='examples')),
                ('File_5', models.FileField(blank=True, upload_to='examples')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_budget', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]