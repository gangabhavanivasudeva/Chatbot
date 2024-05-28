# Generated by Django 3.2.10 on 2021-12-18 07:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dish_name', models.CharField(max_length=200)),
                ('prep_time', models.IntegerField(default=5)),
            ],
        ),
        migrations.CreateModel(
            name='order',
            fields=[
                ('id', models.UUIDField(primary_key=True, serialize=False)),
                ('amount', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='restaurant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ac1', models.BooleanField(default=True)),
                ('takeaway1', models.BooleanField(default=True)),
                ('wifi', models.BooleanField(default=True)),
                ('payment', models.CharField(max_length=200)),
                ('veg', models.BooleanField(default=True)),
                ('can', models.BooleanField(default=True)),
                ('washroom', models.BooleanField(default=True)),
                ('special', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.menu')),
            ],
        ),
    ]
