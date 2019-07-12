from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.template.loader import get_template
from django.conf import settings
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from datetime import datetime

from .models import Reservation
from .forms import ReservationForm
from requestReserv.models import Request


# builds reservation home page
# displays list of all reservations today and in the future
# can choose to edit or delete
# can choose to create a new reservation
@login_required(login_url='/login/')
def reserv_home(request):
    reserv_list = Reservation.objects.all()
    reserv_list = reserv_list.order_by('tour_date', 'tour_time')
    return render(request, 'Reservations/reservationHome.html', {'reservation_list' : reserv_list})

#displays all reservations on a given day
@login_required(login_url='/login/')
def day_list(request, date):
    reserv_list = Reservation.objects.filter(tour_date=date)
    reserv_list = reserv_list.order_by('tour_time')
    return render(request, 'Reservations/list.html', {'reservation_list' : reserv_list})
#displays all reservations
@login_required(login_url='/login/')
def list(request):
    reserv_list = Reservation.objects.all().order_by('tour_date', 'tour_time')
    return render(request, 'Reservations/list.html', {'reservation_list' : reserv_list})


# displays empty form to fill for new reservation
# must be valid to submit
# submit saves to database
@login_required(login_url='/login/')
def reserv_new(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ReservationForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            new_model=form.save(request.POST)
            new_model.save()
            # process the data in form.cleaned_data as required
            # redirect to a new URL, parameter is identity:
            return redirect('reservations:confirm_reservation', pk = new_model.pk)
    # if a GET (or any other method) we'll create a blank form
    else:
        form = ReservationForm()

    return render(request, 'Reservations/addReserv.html', {'form': form})

# displays contents of just created/edited reservation
# can choose to edit or delete
# can send confirmation email
@login_required(login_url='/login/')
def reserv_conf(request, pk):
  entry = get_object_or_404(Reservation, pk=pk)
  return render(request, 'Reservations/confirmReserv.html', {'entry' : entry})

# sends confirmation email for selected entry
#   email host user: TeamSFYL@gmail.com
@login_required(login_url='/login/')
def send_email(request, pk):
    entry = get_object_or_404(Reservation, pk=pk)
    email_template = get_template('Reservations/conf_email.txt')
    conf_email = email_template.render({'entry':entry})
    send_mail(
                subject = 'Confirmation for MoST Reservation',
                message = conf_email,
                from_email = settings.EMAIL_HOST_USER,
                recipient_list = [entry.email, settings.EMAIL_HOST_USER],
                fail_silently = True
    )
    # redirect to reservHome
    reserv_list = Reservation.objects.all()
    return render(request, 'Reservations/reservationHome.html', {'reservation_list' : reserv_list})

# allows user to edit data in selected model 
@login_required(login_url='/login/')
def reserv_edit(request, pk):
    # grab the form
    entry = get_object_or_404(Reservation, pk=pk)
    # procced as if new
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ReservationForm(request.POST, instance=entry)
        # check whether it's valid:
        if form.is_valid():
            new_model=form.save(request.POST)
            new_model.save()
            # process the data in form.cleaned_data as required
            # redirect to a new URL, parameter is identity:
            return redirect('reservations:confirm_reservation', pk = new_model.pk)
    # if a GET (or any other method) we'll create a blank form
    else:
        form = ReservationForm(instance=entry)
    return render(request, 'Reservations/addReserv.html', {'form': form})

# allows user to delete selected reservation
@login_required(login_url='/login/')
def reserv_delete(request, pk):
    # grab and delete object
    entry = get_object_or_404(Reservation, pk=pk)
    entry.delete()
    # return HttpResponse('deleted')
    # proceed to reservation home
    reserv_list = Reservation.objects.all()
    return render(request, 'Reservations/reservationHome.html', {'reservation_list' : reserv_list})

# allows user to edit data in selected model 
# allows user to convert request into a reservation
@login_required(login_url='/login/')
def create(request, pk):
    # grab the form
    entry = get_object_or_404(Request, pk=pk)
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ReservationForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            new_model=form.save(request.POST)
            new_model.save()
            # now delete request
            entry.delete()
            # process the data in form.cleaned_data as required
            # redirect to a new URL, parameter is identity:
            return redirect('reservations:confirm_reservation', pk = new_model.pk)
    # if a GET (or any other method) we'll create a new form
    #   and fill it with fields from the request
    else:
        print(entry.tour_time)
        form = ReservationForm(initial={ 'name': entry.name,
                                         'email': entry.email,
                                         'people_number': entry.people_number,
                                         'tour_time': entry.tour_time,
                                         'tour_date': entry.tour_date,
                                         'Special_Accommodations': entry.Special_Accommodations,
                                        })
    return render(request, 'Reservations/addReserv.html', {'form': form})