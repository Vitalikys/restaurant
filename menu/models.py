import datetime

from django.db import models

from restaurant_user.models import RestaurantUser

WEEKDAY_CHOICE = (
    (0, 'Monday'),
    (1, 'Tuesday'),
    (2, 'Wednesday'),
    (3, 'Thursday'),
    (4, 'Friday'),
    (5, 'Saturday'),
    (6, 'Sunday'),
)


class Menu(models.Model):
    """
    create menu  for each day (only restaurant access)
    """
    id = models.AutoField(primary_key=True)
    week_day = models.IntegerField(choices=WEEKDAY_CHOICE, default=0)
    main_dish = models.CharField(max_length=22, blank=True)
    salads = models.CharField(max_length=22, blank=True)
    drinks = models.CharField(max_length=22, blank=True)
    desserts = models.CharField(max_length=22, blank=True)

    created_at = models.DateTimeField(editable=False, auto_now=datetime.datetime.now())
    updated_at = models.DateTimeField(auto_now=datetime.datetime.now())


class Order(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(RestaurantUser, on_delete=models.CASCADE)
    day_menu = models.DateField(editable=False, auto_now_add=True)
    created_at = models.DateTimeField(editable=False, auto_now=datetime.datetime.now())
    ip = models.CharField(max_length=16, blank=True)
