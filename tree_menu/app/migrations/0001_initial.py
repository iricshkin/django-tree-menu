# Generated by Django 4.1.7 on 2023-03-01 20:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, unique=True, verbose_name='Наименование меню')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание меню')),
                ('slug', models.SlugField(max_length=20, verbose_name='Слаг меню')),
            ],
            options={
                'verbose_name': 'Меню',
                'verbose_name_plural': 'Меню',
            },
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='Наименование пункта меню')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание пункта меню')),
                ('slug', models.SlugField(max_length=20, verbose_name='Слаг пункта меню')),
                ('menu', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='items', to='app.menu', verbose_name='Меню')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='childs', to='app.item', verbose_name='Родительский пункт')),
            ],
            options={
                'verbose_name': 'Пункт меню',
                'verbose_name_plural': 'Пункты меню',
            },
        ),
    ]
