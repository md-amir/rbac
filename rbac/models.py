from django.contrib.auth.models import User
from django.db import models
from builtins import str

from account.models import Organization


class Permission(models.Model):
    name = models.CharField(max_length=50, default="", null=True)
    code_name = models.CharField(max_length=50, default="", null=True)
    description = models.TextField(default='')
    isActive = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Role(models.Model):
    name = models.CharField(max_length=50, default="", null=True)
    permissions = models.ManyToManyField(Permission, through='RolePermission', related_name='role')
    users = models.ManyToManyField(User, through='UserRole')
    description = models.TextField(default='')
    isActive = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class RolePermission(models.Model):
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    permission = models.ForeignKey(Permission, on_delete=models.CASCADE)
    isActive = models.BooleanField(default=True)


class UserRole(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE, null=True,blank=True)
    isActive = models.BooleanField(default=True)
