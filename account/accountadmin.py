from django.contrib import admin

from account.models import Organization


class OrganizationAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Organization._meta.fields]

    class Meta:
        model = Organization
