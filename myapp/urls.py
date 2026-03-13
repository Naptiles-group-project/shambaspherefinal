from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('',views.home,name='home'),
    path('farmer-register/', views.farmer_register, name='farmer_register'),
    path('farmer-dashboard/', views.farmer_dashboard, name='farmer_dashboard'),
    path('farmer-dashboard/', views.farmer_dashboard, name='farmer_dashboard'),
    path('marketplace/', views.marketplace, name='marketplace'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)