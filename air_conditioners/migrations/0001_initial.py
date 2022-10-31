# Generated by Django 4.1 on 2022-09-26 18:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('brands', '0001_initial'),
        ('categories', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AirConditioner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=254, unique=True)),
                ('energy_efficiency', models.CharField(blank=True, max_length=254)),
                ('btu', models.PositiveIntegerField(blank=True, default='0')),
                ('description', models.TextField()),
                ('ac_img', models.FileField(upload_to='ac_img')),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='brands', to='brands.acbrands')),
                ('categorie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='procat', to='categories.categories')),
                ('sub_categorie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='prosubcat', to='categories.subcategories')),
            ],
        ),
    ]
