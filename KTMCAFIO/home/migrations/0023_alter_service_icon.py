# Generated by Django 4.2.4 on 2023-09-24 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0022_remove_order_country_remove_order_pincode_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='icon',
            field=models.URLField(),
        ),
    ]
