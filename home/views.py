from django.shortcuts import render
# Create your views here.

def index(request):
	return render (request, 'index.html',)

def contact_view(request):
  return render(request, 'contactUs.html',)