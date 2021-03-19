from django.contrib import admin

# Register your models here.
from .models import Record


class RecordAdmin(admin.ModelAdmin):
    list_display = ['index', 'operator', 'record_date']
    fieldsets = (
        ('General', {
            'fields': ['index', 'record_date', 'operator']
        }),
        # ('more options', {
        #     'classes': ('collapse',),
        #     'fields': ['record_date', 'operator'],
        # }),
    )


admin.site.register(Record, RecordAdmin)
