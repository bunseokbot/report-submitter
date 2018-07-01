from django.contrib import admin

from .models import Account, College, Major


@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = ('idx', 'account_id', 'account_type', 'email',
                    'name', 'is_active', 'is_admin', )


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
