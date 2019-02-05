from django.contrib import admin

from account.accountadmin import OrganizationAdmin
from account.models import Organization

admin.site.register(Organization, OrganizationAdmin)
