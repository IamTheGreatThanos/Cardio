# Generated by Django 3.0.7 on 2021-03-03 12:44

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CardioApp', '0009_auto_20210210_2113'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProfileData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.CharField(blank=True, max_length=160, null=True)),
                ('data', django.contrib.postgres.fields.ArrayField(base_field=models.BigIntegerField(), blank=True, null=True, size=None)),
            ],
        ),
        migrations.RemoveField(
            model_name='profile',
            name='card_id',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='data',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='date',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='user',
        ),
    ]
