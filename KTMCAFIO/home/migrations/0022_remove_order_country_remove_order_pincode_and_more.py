# Generated by Django 4.2.4 on 2023-09-24 06:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0021_menuitemimage_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='country',
        ),
        migrations.RemoveField(
            model_name='order',
            name='pincode',
        ),
        migrations.RemoveField(
            model_name='order',
            name='state',
        ),
    ]
