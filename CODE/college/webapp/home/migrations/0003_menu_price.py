# Generated by Django 3.2.10 on 2021-12-18 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_restaurant_workinghours'),
    ]

    operations = [
        migrations.AddField(
            model_name='menu',
            name='price',
            field=models.IntegerField(default=0),
        ),
    ]
