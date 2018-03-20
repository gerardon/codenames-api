# Generated by Django 2.0.3 on 2018-03-20 18:12

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0004_auto_20180320_1559'),
    ]

    operations = [
        migrations.AlterField(
            model_name='board',
            name='response_card',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, choices=[('I', 'Innocent'), ('A', 'Assassin'), ('R', 'Red'), ('B', 'Blue')], max_length=20), blank=True, null=True, size=25),
        ),
    ]