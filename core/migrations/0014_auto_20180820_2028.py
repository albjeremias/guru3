# Generated by Django 2.0.8 on 2018-08-20 20:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_auto_20180817_2045'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventoryitem',
            name='barcode',
            field=models.CharField(max_length=32, unique=True, verbose_name='Barcode'),
        ),
    ]