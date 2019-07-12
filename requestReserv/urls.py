from django.conf.urls import re_path, include
from requestReserv import views

app_name = 'requests'

urlpatterns = [
  re_path(r'^$', views.request_new, name ='Requests/requestReserv.html'),
  re_path(r'list/', views.list, name ='list'),
  re_path(r'delete/(?P<pk>\d+)/', views.delete, name ='delete'),
  re_path(r'confirm_request/(?P<pk>\d+)/', views.request_conf, name ='confirmRequest'),
]