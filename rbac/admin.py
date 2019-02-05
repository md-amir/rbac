from django.contrib import admin


from rbac.models import Role, Permission, RolePermission, UserRole
from rbac.rbacadmin import RoleAdmin, PermissionAdmin, RolePermissionAdmin, UserRoleAdmin

admin.site.register(Role, RoleAdmin)
admin.site.register(Permission, PermissionAdmin)
admin.site.register(RolePermission, RolePermissionAdmin)
admin.site.register(UserRole, UserRoleAdmin)