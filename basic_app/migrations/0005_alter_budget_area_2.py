# Generated by Django 4.1 on 2022-09-27 10:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basic_app', '0004_alter_budget_division_1_alter_budget_division_2_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='budget',
            name='Area_2',
            field=models.PositiveIntegerField(blank=True, default='0'),
        ),
    ]
