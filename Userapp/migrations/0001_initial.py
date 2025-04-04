# Generated by Django 5.1.4 on 2024-12-12 09:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Adminapp', '0005_clothes_sub_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='WishList',
            fields=[
                ('wishlist_id', models.AutoField(primary_key=True, serialize=False)),
                ('cloth', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Adminapp.clothes')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Adminapp.register')),
            ],
            options={
                'db_table': 'wish_list_table',
            },
        ),
    ]
