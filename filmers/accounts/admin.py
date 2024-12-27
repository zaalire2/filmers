from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, AdminUser, RegularUser

class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff')
    list_filter = ('is_staff', 'is_superuser', 'is_active')

class AdminUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name')
    
    def get_queryset(self, request):
        return AdminUser.objects.filter(is_staff=True)

    def save_model(self, request, obj, form, change):
        obj.is_staff = True
        super().save_model(request, obj, form, change)

class RegularUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name')
    
    def get_queryset(self, request):
        return RegularUser.objects.filter(is_staff=False)

    def save_model(self, request, obj, form, change):
        obj.is_staff = False
        super().save_model(request, obj, form, change)

admin.site.register(User, CustomUserAdmin)
admin.site.register(AdminUser, AdminUserAdmin)
admin.site.register(RegularUser, RegularUserAdmin) 