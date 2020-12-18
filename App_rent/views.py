from django.shortcuts import render ,HttpResponseRedirect,HttpResponse,get_object_or_404
from django.views.generic import ListView , View ,ListView,DetailView
from .models import Rent , Booking 
from App_rent.forms import BookingForm
from django.urls import reverse
# Create your views here.

class RentList(ListView):
    model = Rent

class BookingList(ListView):
    model=Booking


def AirPortRentList(request):
    Airport_Rent= Rent.objects.filter(pack_category='AIR')
    return render(request, 'App_rent/Airport_rent.html', context={'Airport_Rent':Airport_Rent})
def HourlyRentList(request):
    Hourly_Rent = Rent.objects.filter(pack_category='HRL')
    return render(request, 'App_rent/Hourly_rent.html', context={'Hourly_Rent':Hourly_Rent})

def DailyRentDhakaList(request):
    Daily_Dhaka_Rent = Rent.objects.filter(pack_category='DLD')
    return render(request, 'App_rent/Daily_Dhaka_Rent.html', context={'Daily_Dhaka_Rent':Daily_Dhaka_Rent})

def MonthlyRentList(request):
    Monthly_Rent = Rent.objects.filter(pack_category='MON')
    return render(request, 'App_rent/monthly_rent.html', context={'Monthly_Rent':Monthly_Rent})

# class RentDetail(DetailView):
#     model= Rent 
#     template_name="App_rent/rental_details.html"

def RentDetail(request, pack_category ,pk ):
    item=get_object_or_404(Rent,pack_category=pack_category ,pk=pk)
    form = BookingForm()
    user= request.user
    print(user)
    if request.method== 'POST':
        form=BookingForm(request.POST)
        if form.is_valid():
            booking_form=form.save(commit=False)
            booking_form.rent = item            
            booking_form.user= request.user                     
            booking_form.save()
            return HttpResponseRedirect(reverse('App_rent:show-list'))
    return render(request,'App_rent/rental_details.html',context={'item':item ,'form':form})



def ShopView(request):
    bookings = Booking.objects.filter(user=request.user)

    return render(request,'App_rent/shoplist.html', context={'bookings':bookings})


def about_us(request):
    return render( request, 'App_rent/about.html')

def Home(request):
    return render(request,'base.html')

def Pricing(request):
    return render(request,'App_rent/pricing.html')
def Packages(request):
    return render(request,'App_rent/packages.html')
def Contact(request):
    return render(request,'App_rent/contact.html')