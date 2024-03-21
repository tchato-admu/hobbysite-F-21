from django.contrib import admin

from .models import Comments, Commissions


class CommentsInline(admin.TabularInline):
    model = Comments


class CommissionsAdmin(admin.ModelAdmin):
    model = Commissions
    inlines = [CommentsInline,]


admin.site.register(Commissions, CommissionsAdmin)