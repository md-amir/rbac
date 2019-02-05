from django.contrib import admin

from rbac.models import Role, Permission, RolePermission, UserRole


class RoleAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Role._meta.fields]

    class Meta:
        model = Role


class PermissionAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Permission._meta.fields]

    class Meta:
        model = Permission


class RolePermissionAdmin(admin.ModelAdmin):
    list_display = [f.name for f in RolePermission._meta.fields]

    class Meta:
        model = RolePermission


class UserRoleAdmin(admin.ModelAdmin):
    list_display = [f.name for f in UserRole._meta.fields]

    class Meta:
        model = UserRole
