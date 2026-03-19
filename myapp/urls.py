from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings
from myapp.admin import admin_site  # import your custom admin


urlpatterns = [
    #  path('myadmin/', admin_site.urls),  # use custom admin instead of default admin/
   
    path('', views.home, name='home'),
    path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('farmer-register/', views.farmer_register, name='farmer_register'),
    path('farmer-dashboard/', views.farmer_dashboard, name='farmer_dashboard'),
    path('buyer-register/', views.buyer_register, name='buyer_register'),
    path('buyer-dashboard/', views.buyer_dashboard, name='buyer_dashboard'),
    path('marketplace/', views.marketplace, name='marketplace'),
    path('create-order/', views.create_order, name='create_order'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('edit-produce/<int:produce_id>/', views.edit_produce, name='edit_produce'),
    path('delete-produce/<int:produce_id>/', views.delete_produce, name='delete_produce'),
    path('advisor-register/', views.advisor_register, name='advisor_register'),
    path('dashboard/pending-advisors/', views.pending_advisors, name='pending_advisors'),
    path('dashboard/approve-advisor/<int:advisor_id>/', views.approve_advisor, name='approve_advisor'),
    path('dashboard/reject-advisor/<int:advisor_id>/', views.reject_advisor, name='reject_advisor'),
    path('advisor-dashboard/', views.advisor_dashboard, name='advisor_dashboard'),
    path('suspend-user/<int:user_id>/', views.suspend_user, name='suspend_user'),
    path('create-advisor-post/', views.create_advisor_post, name='create_advisor_post'),
    path('advisory/', views.advisory_feed, name='advisory_feed'),
    path('dashboard/pending-posts/', views.pending_posts, name='pending_posts'),
    path('dashboard/approve-post/<int:post_id>/', views.approve_post, name='approve_post'),
    path('dashboard/reject-post/<int:post_id>/', views.reject_post, name='reject_post'),

  

   

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
