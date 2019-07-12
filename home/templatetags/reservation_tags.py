from django import template

from reservHome.models import Reservation
from datetime import datetime

register = template.Library()

@register.simple_tag
def get_future_set(reservation_list):
    return reservation_list.filter(tour_date__gte=datetime.today())

@register.simple_tag
def get_date_count(reservation_list, date):
    return reservation_list.filter(tour_date=date).count()