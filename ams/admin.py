from django.contrib import admin
from .models import Room_type, Room, Extra, Billing, TenantProfile, MaintenanceCharge
from account.models import CustomUser
from django.contrib.auth.admin import UserAdmin

admin.site.register(Room)
admin.site.register(Room_type)
admin.site.register(Extra)


@admin.register(Billing)
class BillingAdmin(admin.ModelAdmin):
    list_display = (
        'bill_ref', 'room_no', 'tenant_name', 'bill_date', 'overdue_amount', 'bill_total', 'payment_amount',
        'cf_amount',
        'status')
    list_filter = ('bill_ref', 'tenant_name', 'bill_date', 'status')
    search_fields = ('tenant_name', 'bill_ref')


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    # pass # default
    # add_form = CustomUserCreationForm # used by signup in the app
    # form = CustomUserChangeForm
    list_display = ['username', 'first_name', 'last_name', 'is_active', 'is_superuser']


@admin.register(TenantProfile)
class TenantProfileAdmin(admin.ModelAdmin):
    list_display = ['tenant', 'room_no', 'phone', 'pin']


@admin.register(MaintenanceCharge)
class MaintenanceChargeAdmin(admin.ModelAdmin):
    list_display = ['room_no', 'desc', 'job_date', 'status']
