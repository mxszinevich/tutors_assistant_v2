# Generated by Django 3.2.12 on 2022-04-17 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homeworks', '0004_homework_teacher'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homework',
            name='final_day',
            field=models.DateField(verbose_name='Последний день сдачи задания'),
        ),
    ]