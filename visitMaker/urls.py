"""visitMaker URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import url, include
from django.views.generic import RedirectView
from accounts.views import (login_view, register_view, logout_view, list_users)
from home.views import(contact_view)
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^home/', include ('home.urls')) ,
    url(r'^request_reservation/', include('requestReserv.urls')),
    url(r'^reservation_home/', include('reservHome.urls', 'reservations')),
   # url(r'^contact_us/', include('contactUs.urls')),
    url(r'^register/', register_view, name='register'),
    url(r'^contact_us', contact_view , name = 'contactUs.html'),
    url(r'^manage/', list_users, name ='Users/manage.html'),
    url(r'^accounts/', include('accounts.urls', 'accounts')),
    url(r'^login/', login_view, name='login'),
    url(r'^logout/', logout_view, name='logout'),
    url(r'^report_generation/', include('Reports.urls')),
    url(r'^$', RedirectView.as_view(url='/home', permanent = True)),
]