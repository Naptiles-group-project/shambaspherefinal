from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [

    # ================= HOME =================
    path('', views.home, name='home'),

    # ================= AUTH =================
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),

    # ================= ADMIN =================
    path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('suspend-user/<int:user_id>/', views.suspend_user, name='suspend_user'),

    # Orders control
    path('confirm-payment/<int:order_id>/', views.confirm_payment, name='confirm_payment'),
    path('start-delivery/<int:order_id>/', views.start_delivery, name='start_delivery'),

    # ================= FARMER =================
    path('farmer-register/', views.farmer_register, name='farmer_register'),
    path('farmer-dashboard/', views.farmer_dashboard, name='farmer_dashboard'),

    path('edit-produce/<int:produce_id>/', views.edit_produce, name='edit_produce'),
    path('delete-produce/<int:produce_id>/', views.delete_produce, name='delete_produce'),

    # ================= BUYER =================
    path('buyer-register/', views.buyer_register, name='buyer_register'),
    path('buyer-dashboard/', views.buyer_dashboard, name='buyer_dashboard'),

    # Marketplace
    path('marketplace/', views.marketplace, name='marketplace'),

    # Cart system (shared everywhere)
    path('cart/', views.cart_view, name='cart_view'),
    path('add-to-cart/<int:produce_id>/', views.add_to_cart, name='add_to_cart'),
    path('remove-from-cart/<int:item_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('checkout/', views.checkout, name='checkout'),
    path("payment-success/", views.payment_success, name="payment_success"),
    # Delivery confirmation
    path('confirm-delivery/<int:item_id>/', views.confirm_delivery, name='confirm_delivery'),

    # ================= ADVISOR =================
    path('advisor-register/', views.advisor_register, name='advisor_register'),
    path('advisor-dashboard/', views.advisor_dashboard, name='advisor_dashboard'),
    path('create-advisor-post/', views.create_advisor_post, name='create_advisor_post'),
    path('advisory/', views.advisory_feed, name='advisory_feed'),

    # Admin advisor management
    path('dashboard/pending-advisors/', views.pending_advisors, name='pending_advisors'),
    path('dashboard/approve-advisor/<int:advisor_id>/', views.approve_advisor, name='approve_advisor'),
    path('dashboard/reject-advisor/<int:advisor_id>/', views.reject_advisor, name='reject_advisor'),

    # Advisor posts approval
    path('dashboard/pending-posts/', views.pending_posts, name='pending_posts'),
    path('dashboard/approve-post/<int:post_id>/', views.approve_post, name='approve_post'),
    path('dashboard/reject-post/<int:post_id>/', views.reject_post, name='reject_post'),

    # Wallet and withdrawals
    path('wallet/', views.wallet_view, name='wallet_view'),
    path('request-withdrawal/', views.request_withdrawal, name='request_withdrawal'),
    path('mark-withdrawal-paid/<int:withdrawal_id>/', views.mark_withdrawal_paid, name='mark_withdrawal_paid'),

    path('admin-withdrawals/', views.admin_withdrawals, name='admin_withdrawals'),
    path('approve-withdrawal/<int:withdrawal_id>/', views.approve_withdrawal, name='approve_withdrawal'),
    path('mark-withdrawal-paid/<int:withdrawal_id>/', views.mark_withdrawal_paid, name='mark_withdrawal_paid'),
    path('admin-orders/', views.admin_orders, name='admin_orders'),
    path('farmer-orders/', views.farmer_orders, name='farmer_orders'),
    path('farmer-listings/', views.farmer_listings, name='farmer_listings'),
    path('update-delivery-fee/<int:order_id>/', views.update_delivery_fee, name='update_delivery_fee'),
    path("verify-payment/<str:ref>/", views.verify_payment, name="verify_payment"),
    path("success/", views.success_page, name="success_page"),
    path('receipt/<int:order_id>/', views.download_receipt, name='download_receipt'),
    path('dashboard/delete-product/<int:product_id>/', views.admin_delete_product, name='admin_delete_product'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)