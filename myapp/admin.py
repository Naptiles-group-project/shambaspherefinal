from django.contrib import admin
from django.urls import path
from .models import AdvisorPost, AdvisorProfile
from . import views  # make sure you import your views

# Custom Admin Site
class MyAdminSite(admin.AdminSite):
    site_header = "ShambaSphere Admin"

    def get_urls(self):
        urls = super().get_urls()
        my_urls = [
            path('pending-advisors/', views.pending_advisors, name='pending_advisors'),
            path('pending-posts/', views.pending_posts, name='pending_posts'),  # add pending posts URL
        ]
        return my_urls + urls

admin_site = MyAdminSite(name='myadmin')

# Register AdvisorProfile so you can approve/reject advisors
@admin.register(AdvisorProfile, site=admin_site)
class AdvisorProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'specialization', 'status', 'created_at')
    list_filter = ('status',)
    search_fields = ('user__first_name', 'user__last_name', 'specialization')
    ordering = ('-created_at',)

# Register AdvisorPost for admin approval
@admin.register(AdvisorPost, site=admin_site)
class AdvisorPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'advisor', 'status', 'created_at')
    list_filter = ('status', 'category')
    search_fields = ('title', 'content', 'advisor__user__first_name')
    ordering = ('-created_at',)