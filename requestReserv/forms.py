from django import forms
from django.forms import ModelForm, Textarea, SelectDateWidget
from .models import Request

# form completely dependent on base model : Request
class RequestForm(ModelForm):
	class Meta:
		model = Request
		fields = '__all__'
		widgets = {
			'tour_date': SelectDateWidget(),
			'Special_Accommodations': Textarea(),
		}