# Generated by Django 3.1.7 on 2021-03-06 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0013_auto_20210306_1534'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='u_sex',
            field=models.CharField(blank=True, choices=[('0', ''), ('1', 'Мужской'), ('2', 'Женский')], max_length=1, verbose_name='Выберите пол'),
        ),
    ]