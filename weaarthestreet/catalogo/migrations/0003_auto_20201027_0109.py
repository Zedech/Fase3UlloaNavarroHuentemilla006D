# Generated by Django 3.1.2 on 2020-10-27 04:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogo', '0002_auto_20201026_1659'),
    ]

    operations = [
        migrations.AlterField(
            model_name='genero',
            name='marca',
            field=models.CharField(help_text='Ingrese la marca y el tipo de producto EJ: Nike, Zapatilla; adidas, poleron', max_length=100),
        ),
    ]
