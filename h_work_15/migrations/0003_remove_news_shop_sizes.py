# Generated by Django 3.1.7 on 2021-03-03 08:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('h_work_15', '0002_auto_20210303_1327'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='news',
            name='shop_sizes',
        ),
    ]
