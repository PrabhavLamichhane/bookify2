# Generated by Django 2.1.4 on 2019-12-13 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='user',
        ),
        migrations.AddField(
            model_name='account',
            name='email_confirmed',
            field=models.BooleanField(default=False),
        ),
        migrations.DeleteModel(
            name='Profile',
        ),
    ]
