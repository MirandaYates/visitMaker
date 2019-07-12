from django import forms
from django.forms import ModelForm, Textarea, SelectDateWidget
from .models import DateQueryRange, Report, Email

class DateQueryForm(ModelForm):
	class Meta:
		model = DateQueryRange
		fields = '__all__'
		widgets = {
				'start_date' : SelectDateWidget(),
				'end_date' : SelectDateWidget(),
		}

class Email(ModelForm):
	class Meta:
		model = Email
		fields = '__all__'