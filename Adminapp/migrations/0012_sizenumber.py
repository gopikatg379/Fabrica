# Generated by Django 5.1.4 on 2024-12-27 04:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Adminapp', '0011_remove_subcategorycloth_category_gender'),
    ]

    operations = [
        migrations.CreateModel(
            name='SizeNumber',
            fields=[
                ('sizeNumber_id', models.AutoField(primary_key=True, serialize=False)),
                ('number', models.IntegerField()),
            ],
            options={
                'db_table': 'size_number_table',
            },
        ),
    ]
