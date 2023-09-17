# Generated by Django 4.2.4 on 2023-08-09 08:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('email', models.EmailField(max_length=300)),
                ('subject', models.TextField()),
                ('message', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Information',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=400)),
                ('phone', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=500)),
            ],
        ),
    ]
