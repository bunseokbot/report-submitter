from django.contrib import admin

from .models import Account, College, Major
from .forms import AccountCreationForm, AccountChangeForm


@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    form = AccountChangeForm
    add_form = AccountCreationForm

    list_display = ('idx', 'account_id', 'account_type', 'email',
                    'name', 'is_active', 'is_admin', )

    list_filter = ('is_active', 'is_admin', 'account_type', )

    fieldsets = (
        ('Account Information', {'fields': ('account_id', 'account_type', 'password', )}),
        ('Personal Information', {'fields': ('email', 'name', )}),
        ('Permissions', {'fields': ('is_active', 'is_admin', )})
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('account_id', 'email', 'name', 'password1', 'password2')
        }),
    )


@admin.register(College)
class CollegeAdmin(admin.ModelAdmin):
    list_display = ('idx', 'name',)


@admin.register(Major)
class MajorAdmin(admin.ModelAdmin):
    list_display = ('idx', '_get_college', 'name', )

    def _get_college(self, obj):
        try:
            college = College.objects.get(majors=obj)
            return college.name
        except:
            return ''

    _get_college.short_description = 'College'
