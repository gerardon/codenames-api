# Generated by Django 2.0.3 on 2018-03-20 18:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('board', '0005_auto_20180320_1812'),
    ]

    operations = [
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('team', models.CharField(choices=[('R', 'Red'), ('B', 'Blue')], max_length=4)),
                ('is_leader', models.BooleanField(default=False)),
                ('auth_token', models.CharField(max_length=25)),
                ('board', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='board.Board')),
            ],
        ),
    ]