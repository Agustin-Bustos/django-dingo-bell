# Generated by Django 4.2.4 on 2023-11-30 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libreria', '0002_comentarios'),
    ]

    operations = [
        migrations.AddField(
            model_name='libro',
            name='Promo',
            field=models.BooleanField(null=True, verbose_name='Promo'),
        ),
    ]
