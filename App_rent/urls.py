from django.urls import path
from .views import Home, about_us , RentList,BookingList,AirPortRentList ,HourlyRentList ,DailyRentDhakaList,MonthlyRentList, RentDetail,ShopView,Pricing,Packages,Contact
app_name= 'App_rent'

urlpatterns=[

   path('',Home , name='Home'),
   path('about_us/',about_us, name='about_us'),

   
   path('rent_list/', RentList.as_view(),name='RentList'),
   path('book_list/',BookingList.as_view(),name='BookList'),
   path('airport_rent/',AirPortRentList,name='Airport-rent'),
   path('hourly_rent/',HourlyRentList,name='hourly-rent'),
   path('daily_dhaka_rent/',DailyRentDhakaList,name='daily-dhaka-rent'),
   path('monthly_rent/',MonthlyRentList,name='monthly-rent'),
   path('rent_details/<pack_category>/<pk>/', RentDetail,name='rent-details'),
   path('booking_list/',ShopView,name='show-list'),
   path('pricing/',Pricing,name='pricing'),
   path('packages/',Packages,name='packages'),
   path('contact/',Contact,name='contact'),



   # path('rent_details/<pack_category>/<pk>/', RentDetail.as_view(),name='rent-details'),

   # path('rent_details/<pack_category>', RentDetails.as_view(),name='RentdetailsList'),
   
    
]
