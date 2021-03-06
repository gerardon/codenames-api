# Generated by Django 2.0.3 on 2018-03-20 07:14

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Board',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('invite_code', models.CharField(max_length=25)),
                ('words', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=10), size=25)),
            ],
        ),
    ]
