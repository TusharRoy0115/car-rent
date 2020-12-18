# Generated by Django 3.1.4 on 2020-12-14 07:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Rent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pack_category', models.CharField(choices=[('AIR', 'AIRPORT'), ('DLD', 'DAILY-DHAKA'), ('DLO', 'DAILY-OUTSIDE'), ('HRL', 'HOURLY'), ('MON', 'MONTHLY'), ('OFC', 'OFFICE')], max_length=3)),
                ('car_category', models.CharField(choices=[('SSD', 'STANDARD-SEDAN'), ('PSD', 'PREMIUM-SEDAN'), ('HIC', 'HIACE'), ('NOH', 'NOAH'), ('AXO', 'TOYOTA-AXIO'), ('ALN', 'TOYOTA-ALION'), ('NHH', 'NOAH-HYBRID'), ('PRM', 'PREMIO'), ('BUS', 'MINI-BUS'), ('CRS', 'LAND-CRUISER')], max_length=3)),
                ('image', models.ImageField(upload_to='images')),
            ],
        ),
    ]