from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.template.loader import get_template
from django.conf import settings
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.utils.timezone import datetime

from .models import DateQueryRange , Report , Email
from .forms import DateQueryForm, Email

from reservHome.models import Reservation

"""

def report_generate(request)
	if request.method == 'POST':

		form = ReportForm(request.POST)

		if form.is_valid():
			new_model = form.save(request.post)
			new_.model.save()

			return redirect()

"""


# Create your views here.
@login_required(login_url='/login/')
def query_dateRange(request):

	if request.method == 'POST':

		form = DateQueryForm(request.POST)

		if form.is_valid():
			new_model = form.save(commit=False)
			new_model.save()

			return redirect('reports:generated_report' , pk = new_model.pk)
	else:
		form = DateQueryForm()

	return render(request, 'Reports/report_request_date.html', {'form' : form })

@login_required(login_url='/login/')
def report_generation(request, pk):
	dates = get_object_or_404(DateQueryRange , pk = pk)

	test_entries = Reservation.objects.all()
	req_date = datetime.today()
	filteredReservations = test_entries.filter(creation_date__range=[dates.start_date, dates.end_date])
	filteredTours = test_entries.filter(tour_date__range = [dates.start_date, dates.end_date])

	num_tours = 0
	num_visitors = 0
	for entries in filteredTours:
  		num_tours += 1
  		num_visitors += entries.people_number

	num_reservations = 0
	for entries in filteredReservations:
  		num_reservations += 1


	form = Report(start_date = dates.start_date , end_date = dates.end_date , request_date = req_date\
	, number_of_tours = num_tours , number_of_reservations = num_reservations\
	, number_of_visitors = num_visitors ,)
	form.save()


	nameOfFile = "(" + str(dates.start_date) + ")-(" + str(dates.end_date) + ").txt"
	fileAddress = "./Reports/Generated_Reports/" + nameOfFile
	file = open(fileAddress, 'w')
	file.write("REPORT GENERATED ON: " + str(req_date) + "\n\n")
	file.write("Total number of tours taking place: " + str(num_tours) + "\n")
	file.write("Total number of visitors expected: " + str(num_visitors) + "\n")
	file.write("Total number of reservations made: " + str(num_reservations) + "\n")
	file.write("\nListed reservations:\n")

	count = 1;
	for reservation in filteredTours:
		file.write(str(count) + ":")
		file.write("\nCreation Date: " + str(reservation.creation_date))
		file.write("\nDocent: " + str(reservation.docent))
		file.write("\nName: " + str(reservation.name))
		file.write("\nE-mail: " + str(reservation.email))
		file.write("\nTime: " + str(reservation.get_tour_time_display()))
		file.write("\nSpecial Accommodations: " + str(reservation.Special_Accommodations) + "\n\n")
		count += 1
	file.close();



	if request.method == 'POST':

		email = Email(request.POST)
	
		if email.is_valid():

			new_model = email.save(commit=False)
			new_model.save()
			return redirect('reports:confirmation', {'email' : email})
	else:
		email = Email()


	return render(request, 'Reports/report_display.html', {'form' : form})