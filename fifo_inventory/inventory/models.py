from django.db import models
from datetime import date


class Bought(models.Model):
    # Adds current date on insert
    # I am assuming from the example that this is a unique field therefore a primary key
    date = models.DateField(default=date.today, primary_key=True)

    quantity = models.IntegerField()
    cost_per_item = models.FloatField()


class Sold(models.Model):
    date = models.DateField(default=date.today, primary_key=True)
    quantity = models.IntegerField()