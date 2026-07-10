from django import forms
from .models import Booking

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['event_name', 'event_date', 'event_time', 'event_location', 
                  'event_type', 'guests_count', 'special_requests']
        widgets = {
            'event_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'event_time': forms.TimeInput(attrs={'type': 'time', 'class': 'form-control'}),
            'event_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g. Wedding Ceremony'}),
            'event_location': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Event Venue Address'}),
            'event_type': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g. Wedding, Corporate, Birthday'}),
            'guests_count': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Expected number of guests'}),
            'special_requests': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Any special requirements...'}),
        }