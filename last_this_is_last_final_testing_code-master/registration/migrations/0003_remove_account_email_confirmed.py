# Generated by Django 2.1.4 on 2019-12-13 15:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0002_auto_20191213_2049'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='email_confirmed',
        ),
    ]