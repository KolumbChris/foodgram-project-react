# Generated by Django 4.2.7 on 2023-12-12 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='password',
            field=models.CharField(help_text='Введите пароль пользователя', max_length=150, verbose_name='Пароль'),
        ),
    ]
