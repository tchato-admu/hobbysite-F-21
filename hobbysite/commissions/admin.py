from django.contrib import admin

from .models import Comment, Commission


class CommentInline(admin.TabularInline):
    model = Comment


class CommissionAdmin(admin.ModelAdmin):
    model = Commission
    inlines = [CommentInline]


admin.site.register(Commission, CommissionAdmin)