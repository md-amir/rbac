from django.contrib.auth.models import User
from django.db import models
from builtins import str


class Address(models.Model):
    street_one = models.CharField(max_length=100, default='', blank=True, null=True)
    street_two = models.CharField(max_length=100, default='', blank=True, null=True)
    street_three = models.CharField(max_length=100, default='', blank=True, null=True)
    mobile = models.CharField(max_length=30, blank=True, null=True, default=None, )
    website = models.CharField(max_length=50, default='', blank=True, null=True)
    email = models.EmailField(blank=True, null=True, default=None, )
    state = models.CharField(max_length=20, default='', blank=True)
    zip = models.CharField(max_length=5, default="", blank=True)
    city = models.CharField(max_length=20, default="", blank=True)

    country = models.CharField(max_length=20, default="", blank=True)
    area = models.CharField(max_length=10, default="", blank=True)

    # objects = models.Manager()
    # gis = gis_models.GeoManager()

    def __str__(self):
        return str(self.id) + ' address'


class Organization(models.Model):
    name = models.CharField(max_length=100, default='')
    owner = models.ForeignKey(User, null=True, on_delete="SET_NULL", related_name='organization')

    def __str__(self):
        return self.name

    def get_name(self):
        return self.name
