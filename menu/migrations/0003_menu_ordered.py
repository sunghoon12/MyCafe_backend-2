# Generated by Django 3.2.7 on 2021-10-11 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0002_menu_stocked'),
    ]

    operations = [
        migrations.AddField(
            model_name='menu',
            name='ordered',
            field=models.BooleanField(default=False),
        ),
    ]
