# Generated by Django 3.1.4 on 2020-12-15 06:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('App_rent', '0003_rent_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rent',
            name='price',
        ),
    ]