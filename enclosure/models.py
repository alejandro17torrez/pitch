from django.db import models


# Create your models here.
class Enclosure(models.Model):
    name = models.CharField(null=True, blank=True, max_length = 255)
    address = models.CharField(null=True, blank=True, max_length = 255)
    desciption = models.CharField(null=True, blank=True, max_length = 255)
    image = models.CharField(null=True, blank=True, max_length = 255)
    latitude = models.CharField(null=True, blank=True, max_length = 255)
    longitude = models.CharField(null=True, blank=True, max_length = 255)
    rate = models.IntegerField(null=True, blank=True)
    distrit = models.IntegerField(null=True, blank=True)
    cash = models.BooleanField(null=True, blank=True)
    credit = models.BooleanField(null=True, blank=True)
    transfer = models.BooleanField(null=True, blank=True)
    court_owner =  models.IntegerField(null=True, blank=True)
    from_noon = models.TimeField(null=True, blank=True)
    to_noon = models.TimeField(null=True, blank=True)
    from_afternoon = models.TimeField(null=True, blank=True)
    to_afternoon = models.TimeField(null=True, blank=True)
    hour_limit = models.IntegerField(null=True, blank=True, default=0)
    deposit = models.DecimalField(max_digits = 5, decimal_places = 2, default=0)
    payment_contribution = models.DecimalField(max_digits = 5, decimal_places = 2, default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __repr__(self):
        return self.__str__()

    


