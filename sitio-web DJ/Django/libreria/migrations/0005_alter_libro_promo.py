# Generated by Django 4.2.4 on 2023-11-30 19:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libreria', '0004_alter_libro_promo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='libro',
            name='Promo',
            field=models.DateTimeField(null=True, verbose_name='Promo'),
        ),
    ]
