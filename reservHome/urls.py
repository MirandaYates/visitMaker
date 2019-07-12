from django.conf.urls import re_path, include
from django.urls import path
from reservHome import views

app_name = 'reservations'

urlpatterns = [
	path('add_reservation/', views.reserv_new, name ='add_reservation'),
	# (route, view, kwargs=NONE, name=NONE)
    re_path(r'confirm_reservation/(?P<pk>\d+)/', views.reserv_conf, name ='confirm_reservation'),
    re_path(r'send_email/(?P<pk>\d+)/', views.send_email, name ='send_email'),
    re_path(r'edit/(?P<pk>\d+)/', views.reserv_edit, name ='edit'),
    re_path(r'delete/(?P<pk>\d+)/', views.reserv_delete, name ='delete'),
    re_path(r'day_list/(?P<date>[0-9]{4}-?[0-9]{2}-?[0-9]{2})/', views.day_list, name ='day_list'),
    re_path(r'list/', views.list, name ='list'),
    re_path(r'create/(?P<pk>\d+)/',views.create, name = 'create'),
	re_path(r'', views.reserv_home, name ='Reservations/reservationHome.html'),
]