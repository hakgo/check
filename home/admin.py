from django.contrib import admin

from .models import *

class MeetingAttendanceInline(admin.TabularInline):
    model = MeetingAttendance
    extra = 1

class MeetingAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Topic', {'fields': ['title']}),
        ('date', {'fields': ['meeting_date']}),
    ]

    inlines = [MeetingAttendanceInline]

admin.site.register(Meeting, MeetingAdmin)
