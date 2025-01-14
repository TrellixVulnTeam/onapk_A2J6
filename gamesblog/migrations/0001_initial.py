# Generated by Django 3.0.2 on 2020-01-14 09:20

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Gamesblog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('pub_date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('image', models.ImageField(upload_to='images/')),
                ('description', models.TextField(blank=True)),
                ('features', models.TextField(blank=True)),
                ('install_steps', models.TextField(blank=True)),
                ('link', models.CharField(max_length=200)),
                ('views', models.IntegerField(default=0)),
            ],
        ),
    ]
