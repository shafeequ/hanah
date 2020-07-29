# Create your models here.
from django.db import models


class Vendor(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    name = models.CharField(max_length=90)
    url = models.CharField(max_length=200, null=True, blank=True, default='')
    service_email = models.EmailField(max_length=120)
    service_phone = models.CharField(max_length=12)
    image = models.CharField(max_length=200, null=True, blank=True, default='')
    terms = models.TextField(blank=True)
    bill_country = models.CharField(max_length=2)
    country_of_residence = models.CharField(max_length=2)
    activation_date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-name"]

    def __str__(self):
        return self.name
