from django.db import models


class AbstractBaseModel(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Location(models.Model):
    latitude = models.DecimalField(max_digits=15, decimal_places=10, default=0.00)
    longitude = models.DecimalField(max_digits=15, decimal_places=10, default=0.00)

    class Meta:
        abstract = True

