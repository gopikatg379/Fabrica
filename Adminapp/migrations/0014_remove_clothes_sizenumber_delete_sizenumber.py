# Generated by Django 5.1.4 on 2024-12-27 05:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Adminapp', '0013_clothes_sizenumber'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='clothes',
            name='sizeNumber',
        ),
        migrations.DeleteModel(
            name='SizeNumber',
        ),
    ]