from django import forms
from django.forms import ModelForm, Textarea, SelectDateWidget
from .models import Reservation

# form completely dependent on base model: Request
class ReservationForm(ModelForm):
	class Meta:
		model = Reservation
		fields = '__all__'
		widgets = {
			'tour_date': SelectDateWidget(),
			'Special_Accommodations': Textarea(),
		}