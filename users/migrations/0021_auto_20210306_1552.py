# Generated by Django 3.1.7 on 2021-03-06 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0020_auto_20210306_1552'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='u_sex',
            field=models.CharField(default=None, max_length=1),
        ),
    ]