# Generated by Django 4.2.4 on 2023-11-30 19:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libreria', '0003_libro_promo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='libro',
            name='Promo',
            field=models.DateField(null=True, verbose_name='Promo'),
        ),
    ]
