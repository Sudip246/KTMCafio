# Generated by Django 4.2.4 on 2023-09-25 11:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0024_alter_service_icon'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='items_img',
            field=models.ForeignKey(default=5, on_delete=django.db.models.deletion.CASCADE, to='home.menuitemimage'),
            preserve_default=False,
        ),
    ]
