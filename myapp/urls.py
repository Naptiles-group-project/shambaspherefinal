from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings



urlpatterns = [
    path('', views.home, name='home'),
    path('farmer-register/', views.farmer_register, name='farmer_register'),
    path('farmer-dashboard/', views.farmer_dashboard, name='farmer_dashboard'),
    path('marketplace/', views.marketplace, name='marketplace'),
    path('create-order/', views.create_order, name='create_order'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('edit-produce/<int:produce_id>/', views.edit_produce, name='edit_produce'),
    path('delete-produce/<int:produce_id>/', views.delete_produce, name='delete_produce'),
    path('buyer-register/', views.buyer_register, name='buyer_register'),
    path('advisor-register/', views.advisor_register, name='advisor_register'),

    # path('advisor-dashboard/', views.advisor_dashboard, name='advisor_dashboard'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
