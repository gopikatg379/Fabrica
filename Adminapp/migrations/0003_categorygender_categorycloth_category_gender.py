# Generated by Django 5.1.4 on 2024-12-09 05:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Adminapp', '0002_register_password'),
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryGender',
            fields=[
                ('categoryGender_id', models.AutoField(primary_key=True, serialize=False)),
                ('categoryGender_name', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'category_gender_table',
            },
        ),
        migrations.AddField(
            model_name='categorycloth',
            name='category_gender',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Adminapp.categorygender'),
        ),
    ]
