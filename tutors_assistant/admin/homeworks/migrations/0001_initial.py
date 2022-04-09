# Generated by Django 3.2.12 on 2022-04-09 18:57

import admin.homeworks.utils
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HomeWork',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=300, verbose_name='Название домашнего задания')),
                ('description', models.TextField(blank=True, max_length=500, verbose_name='Описание')),
                ('score', models.PositiveSmallIntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)], verbose_name='Оценка')),
                ('final_day', models.DateTimeField(verbose_name='Последний день сдачи задания')),
                ('active', models.BooleanField(default=True, verbose_name='Задание активно')),
                ('count_days_delay', models.PositiveSmallIntegerField(default=0, verbose_name='Количество дней опоздания')),
            ],
            options={
                'verbose_name': 'Домашнее задание',
                'verbose_name_plural': 'Домашние задания',
            },
        ),
        migrations.CreateModel(
            name='HomeWorkModule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Модуль домашнего задания')),
                ('description', models.TextField(blank=True, max_length=200, verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Модуль домашнего задания',
                'verbose_name_plural': 'Модули домашнего задания',
            },
        ),
        migrations.CreateModel(
            name='HomeworkFiles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(blank=True, max_length=200, verbose_name='Задание')),
                ('file', models.FileField(blank=True, null=True, upload_to=admin.homeworks.utils.get_directory_path, verbose_name='Фаил')),
                ('homework', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='homeworks.homework', verbose_name='Домашняя работа')),
            ],
            options={
                'verbose_name': 'Фаил домашнего задания',
                'verbose_name_plural': 'Файлы домашнего задания',
            },
        ),
        migrations.CreateModel(
            name='HomeworkAnswer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(blank=True, max_length=200, verbose_name='Задание')),
                ('file', models.FileField(blank=True, null=True, upload_to=admin.homeworks.utils.get_directory_path, verbose_name='Фаил')),
                ('homework', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='homeworks.homework', verbose_name='Домашняя работа')),
            ],
            options={
                'verbose_name': 'Ответ на домашнее задание',
                'verbose_name_plural': 'Ответы на домашнее задание',
            },
        ),
        migrations.AddField(
            model_name='homework',
            name='module',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='homeworks.homeworkmodule', verbose_name='Модуль задания'),
        ),
    ]
