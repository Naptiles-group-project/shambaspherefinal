from django.contrib import admin
from django.urls import path
from .models import AdvisorPost, AdvisorProfile
from . import admin_views  

class MyAdminSite(admin.AdminSite):
    site_header = "ShambaSphere Admin"

    def get_urls(self):
        urls = super().get_urls()
        my_urls = [
            path('pending-advisors/', admin_views.pending_advisors, name='pending_advisors'),
            path('pending-posts/', admin_views.pending_posts, name='pending_posts'),
        ]
        return my_urls + urls

admin_site = MyAdminSite(name='myadmin')


@admin.register(AdvisorProfile, site=admin_site)
class AdvisorProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'specialization', 'status', 'created_at')


@admin.register(AdvisorPost, site=admin_site)
class AdvisorPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'advisor', 'status', 'created_at')