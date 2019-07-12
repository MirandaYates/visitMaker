from django.conf.urls import re_path, include
from django.urls import path
from accounts import views

app_name = 'accounts'

urlpatterns = [
    re_path(r'delete/(?P<pk>\d+)/', views.user_delete, name ='delete'),
]