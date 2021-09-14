from django.db import models
from django.forms import widgets
from django.contrib.auth.models import User


# Create your models here.


# class NewBusinessModel(models.Model):
#     business_registered = models.BooleanField(null=True)


class BusinessModel(models.Model):

    business_name = models.CharField(max_length=100)
    business_logo = models.ImageField(
        upload_to='business_logo', blank=True, null=True)
    business_contact = models.CharField(max_length=100)
    business_email = models.EmailField(max_length=100)
    business_website = models.URLField(max_length=100)
    business_unit_number = models.CharField(
        max_length=100, blank=True, null=True)
    business_street_number = models.CharField(max_length=100)
    business_street_name = models.CharField(max_length=100)
    business_suburb = models.CharField(max_length=100)
    business_postcode = models.CharField(max_length=100)
    business_state = models.CharField(max_length=50)
    business_country = models.CharField(max_length=50)
    business_registered = models.BooleanField(
        default=False, blank=True, null=True)

    class Meta:
        unique_together = [['business_name', 'business_email']]

    def __str__(self):
        return self.business_name
