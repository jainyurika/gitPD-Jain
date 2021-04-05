from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from accounts.models import Account

# Register your models here.
class AccountAdmin(UserAdmin):

    ordering = ('username',)
    list_display = ('username', 'email', 'date_joined', 'last_login',)
    search_fields = ('username', 'email')
    readonly_fields = ('id', 'date_joined', 'last_login')
    
    filter_horizontal = ()
    list_filter = ()
    
    fieldsets = (
        ('Credentials',{'fields': ('username', 'password')}),
        ('Details',{'fields': ('email', 'dob', 'experience', 'phone', 'about')}),
        ('Logs',{'fields': ('date_joined', 'last_login')}),
        ('Permissions',{'fields': ('is_admin', 'is_staff')}),
    )
    add_fieldsets = (
        ('Credentials',{'fields': ('username', 'password')}),
        ('Details',{'fields': ('email', 'dob', 'experience', 'phone', 'about')}),
    )
    # inlines = (UserDepartmentInline, UserVendorInline)
admin.site.register(Account, AccountAdmin)