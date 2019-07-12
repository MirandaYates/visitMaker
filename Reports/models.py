from django.db import models

"""
class Report(models.Model):


	#Beginning date for a range of dates.
 	start_date = models.DateField()

 	#End date for a range of dates.
 	end_date = models.DateField()

 	#Number of total tours in a given time frame.
	num_tours = models.PositiveIntegerField()

	#Number of reservations made in a given time frame.
	num_Reservations = models.PositiveIntegerField()

	#Number of visitors that attended a tour in a given time frame.
	num_visitors = models.PositiveIntegerField()

"""


# Create your models here.
class DateQueryRange(models.Model):
 	#Beginning date for a range of dates.
 	start_date = models.DateField()

 	#End date for a range of dates.
 	end_date = models.DateField()



class Report(models.Model):

	#Beginning date for a range of dates.
	start_date = models.DateField()

 	#End date for a range of dates.
	end_date = models.DateField()

	#Date that report was requested
	request_date = models.DateField()


	#Number of total tours in a given time frame.
	number_of_tours = models.PositiveIntegerField()

	#Number of reservations made in a given time frame.
	number_of_reservations = models.PositiveIntegerField()

	#Number of visitors that attended a tour in a given time frame.
	number_of_visitors = models.PositiveIntegerField()

class Email(models.Model):
	email = models.EmailField()
	filename = models.CharField(max_length=20)

