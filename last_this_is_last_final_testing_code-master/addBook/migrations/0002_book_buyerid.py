# Generated by Django 2.2.7 on 2019-12-09 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('addBook', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='buyerid',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]