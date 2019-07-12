from django.conf.urls import re_path, include
from Reports import views

app_name = 'reports'


urlpatterns = [
	re_path(r'^$', views.query_dateRange, name = 'Reports/report_request_date.html'),
	re_path(r'generated_report/(?P<pk>\d+)/', views.report_generation, name = 'generated_report'),
]