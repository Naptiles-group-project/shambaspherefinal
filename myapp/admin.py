from django.contrib import admin

# Register your models here.
from django.urls import path


from . import views
class MyAdminSite(admin.AdminSite):
    site_header = "ShambaSphere Admin"

    def get_urls(self):
        urls = super().get_urls()
        my_urls = [
            path('pending-advisors/', views.pending_advisors, name='pending_advisors'),
        ]
        return my_urls + urls

admin_site = MyAdminSite(name='myadmin')