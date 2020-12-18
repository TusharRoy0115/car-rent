from django import forms
from App_rent.models import Booking

class BookingForm(forms.ModelForm):
    check_in = forms.DateTimeField(required=True, input_formats=['%Y-%m-%dT%H:%M', ])
    check_out = forms.DateTimeField(required=True, input_formats=['%Y-%m-%dT%H:%M', ])
    class Meta:
        model = Booking
        fields= ('check_in','check_out')
    