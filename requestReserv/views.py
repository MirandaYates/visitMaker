from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404

from django.contrib.auth.decorators import login_required
from django.conf import settings

from .models import Request
from .forms import RequestForm


#displays all requests
@login_required(login_url='/login/')
def list(request):
    request_list = Request.objects.all().order_by('tour_date', 'tour_time')
    return render(request, 'Requests/list.html', {'entries' : request_list})

# displays empty form to fill for new reservation
# must be valid to submit
# submit saves to database
def request_new(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = RequestForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            new_model=form.save(request.POST)
            new_model.save()
            # redirect to a new URL:
            return redirect('requests:confirmRequest', pk = new_model.pk)

    # if a GET (or any other method) we'll create a blank form
    else:
        form = RequestForm()
    return render(request, 'Requests/requestReserv.html', {'form': form})

# displays contents of just created request
def request_conf(request, pk):
  entry = get_object_or_404(Request, pk=pk)
  return render(request, 'Requests/confirmRequest.html', {'entry' : entry})

# allows user to delete selected model
@login_required(login_url='/login/')
def delete(request, pk):
    # grab and delete object
    entry = get_object_or_404(Request, pk=pk)
    entry.delete()
    # return HttpResponse('deleted')
    # proceed to reservatio home
    request_list = Request.objects.all()
    return render(request, 'Requests/list.html', {'entries' : request_list})