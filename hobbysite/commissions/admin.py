from django.contrib import admin

from .models import Job, Commission, JobApplication


class JobInline(admin.TabularInline):
    model = Job


class CommissionsAdmin(admin.ModelAdmin):
    model = Commission
    inlines = [JobInline,]


class JobApplicationAdmin(admin.ModelAdmin):
    model = JobApplication


admin.site.register(JobApplication, JobApplicationAdmin)
admin.site.register(Commission, CommissionsAdmin)
