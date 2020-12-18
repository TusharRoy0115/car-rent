from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Rent (models.Model):
    PACKAGES_CATEGORIES = (
        ('AIR','AIRPORT'),
        ('DLD','DAILY-DHAKA'),
        ('DLO','DAILY-OUTSIDE'),
        ('HRL','HOURLY'),
        ('MON','MONTHLY'),
        ('OFC','OFFICE'),
    )
    CAR_CATEGORIES = (
        ('SSD','STANDARD-SEDAN'),
        ('PSD','PREMIUM-SEDAN'),
        ('HIC','HIACE'),
        ('NOH','NOAH'),
        ('AXO','TOYOTA-AXIO'),
        ('ALN','TOYOTA-ALION'),
        ('NHH','NOAH-HYBRID'),
        ('PRM','PREMIO'),
        ('BUS','MINI-BUS'),
        ('CRS','LAND-CRUISER'),
        
       )
    pack_category = models.CharField(max_length=3,choices=PACKAGES_CATEGORIES)
    car_category = models.CharField(max_length=3,choices=CAR_CATEGORIES)
    price = models.FloatField(default=1500)
    image=models.ImageField(upload_to='images')


    def __str__(self):
        return f'{self.id} {self.pack_category} with car {self.car_category} price {self.price}'



class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE , related_name='user_booking')
    rent = models.ForeignKey(Rent,on_delete=models.CASCADE , related_name='rent')
    check_in = models.DateTimeField()
    check_out = models.DateTimeField()

    class Meta:
        ordering = ('-check_in',)
    

    def __str__(self):
        return f'{self.user} booked {self.rent} from {self.check_in} to {self.check_out} '