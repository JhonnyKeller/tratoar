# Generated by Django 4.1 on 2022-10-30 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basic_app', '0006_remove_budget_user_budget_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='budget',
            name='budget_text',
            field=models.TextField(default='Por favor faça uma breve descrição.', verbose_name='Descrição:'),
        ),
    ]
