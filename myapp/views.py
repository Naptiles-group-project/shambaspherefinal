from decimal import Decimal
from multiprocessing import context
from decimal import Decimal
from django.contrib import messages
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth import authenticate, login, logout as auth_logout
from django.contrib.auth import login as auth_login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.csrf import csrf_protect, ensure_csrf_cookie

from .models import (
    AdvisorPost,
    AdvisorProfile,
    Cart,
    CartItem,
    FarmerProfile,
    Order,
    OrderItem,
    Produce,
    Withdrawal,
)


# Create your views here.

# =========================
# HOME
# =========================
def home(request):
    return render(request, "index.html")


# =========================
# AUTH
# =========================

# def login_view(request):
#     if request.method == "POST":
#         username = request.POST.get("username")
#         password = request.POST.get("password")
#
#         user = authenticate(request, username=username, password=password)
#
#         if user is not None:
#             auth_login(request, user)
#
#             if user.is_superuser:
#                 return redirect("/admin/")
#
#             if FarmerProfile.objects.filter(user=user).exists():
#                 return redirect("farmer_dashboard")
#
#             # Add other roles like AdvisorProfile if needed
#             # if AdvisorProfile.objects.filter(user=user).exists():
#             #     return redirect("advisor_dashboard")
#
#             # Default: Buyer
#             return redirect("marketplace")
#
#         else:
#             messages.error(request, "Invalid username or password")
#
#     return render(request, "login.html")

def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            auth_login(request, user)

            if user.is_superuser:
                return redirect("admin_dashboard")

            if FarmerProfile.objects.filter(user=user).exists():
                return redirect("farmer_dashboard")

            if AdvisorProfile.objects.filter(user=user).exists():
                return redirect("advisor_dashboard")

            return redirect("buyer_dashboard")

        messages.error(request, "Invalid username or password")

    return render(request, "login.html")


def logout_view(request):
    auth_logout(request)
    return redirect("login")


# =========================
# FARMER REGISTER
# =========================

# def farmer_register(request):
#     if request.method == "POST":
#         # Personal Info
#         first_name = request.POST.get("firstName")
#         last_name = request.POST.get("lastName")
#         username = request.POST.get("username")
#         email = request.POST.get("email")
#         phone = request.POST.get("phone")
#         county = request.POST.get("county")
#
#         # Farm Info
#         farm_name = request.POST.get("farmName")
#         farming_type = request.POST.get("farmingType")
#         farm_size = request.POST.get("farmSize")
#         experience = request.POST.get("experience")
#         farm_description = request.POST.get("farmDescription")
#
#         # Produce Categories (checkboxes)
#         produce_categories = request.POST.getlist("produceCategories")
#         produce_categories_str = ",".join(produce_categories)
#
#         # Availability & Security
#         active_status = request.POST.get("activeStatus")

# def farmer_register(request):
#     if request.method == "POST":
#         # Personal Info
#         first_name = request.POST.get("firstName")
#         last_name = request.POST.get("lastName")
#         username = request.POST.get("username")
#         email = request.POST.get("email")
#         phone = request.POST.get("phone")
#         county = request.POST.get("county")
#
#         # Farm Info
#         farm_name = request.POST.get("farmName")
#         farming_type = request.POST.get("farmingType")
#         farm_size = request.POST.get("farmSize")
#         experience = request.POST.get("experience")
#         farm_description = request.POST.get("farmDescription")
#
#         # Produce Categories (checkboxes)
#         produce_categories = request.POST.getlist("produceCategories")
#         produce_categories_str = ",".join(produce_categories)
#
#         # Availability & Security
#         active_status = request.POST.get("activeStatus")
#         harvest_season = request.POST.get("harvestSeason")
#         delivery = request.POST.get("delivery")
#         password = request.POST.get("password")
#
#         # Profile Picture
#         profile_pic = request.FILES.get("profilePic")
#
#         # Check username
#         if User.objects.filter(username=username).exists():
#             return JsonResponse({"success": False, "error": "Username already exists"})
#
#         # Create user
#         user = User.objects.create_user(
#             username=username,
#             email=email,
#             password=password,
#             first_name=first_name,
#             last_name=last_name
#         )
#
#         # Create FarmerProfile
#         FarmerProfile.objects.create(
#             user=user,
#             phone=phone,
#             county=county,
#             profile_pic=profile_pic,
#             farm_name=farm_name,
#             farming_type=farming_type,
#             farm_size=float(farm_size) if farm_size else 0,
#             experience=int(experience) if experience else 0,
#             farm_description=farm_description,
#             produce_categories=produce_categories_str,
#             active_status=active_status,
#             harvest_season=harvest_season,
#             delivery=delivery
#         )
#
#         # Auto-login
#         login(request, user)
#
#         return JsonResponse({"success": True, "redirect_url": "/farmer-dashboard/"})
#
#     return render(request, "farmer-register.html")

def farmer_register(request):
    if request.method == "POST":
        first_name = request.POST.get("firstName")
        last_name = request.POST.get("lastName")
        username = request.POST.get("username")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        county = request.POST.get("county")

        farm_name = request.POST.get("farmName")
        farming_type = request.POST.get("farmingType")
        farm_size = request.POST.get("farmSize")
        experience = request.POST.get("experience")
        farm_description = request.POST.get("farmDescription")

        produce_categories = request.POST.getlist("produceCategories")
        produce_categories_str = ",".join(produce_categories)

        active_status = request.POST.get("activeStatus")
        harvest_season = request.POST.get("harvestSeason")
        delivery = request.POST.get("delivery")
        password = request.POST.get("password")

        profile_pic = request.FILES.get("profilePic")

        if User.objects.filter(username=username).exists():
            return redirect("farmer_dashboard")

        user = User.objects.create_user(
            username=username,
            email=email,
            password=password,
            first_name=first_name,
            last_name=last_name,
        )
        profile_pic = request.FILES.get("profilePic")

        FarmerProfile.objects.create(
            user=user,
            phone=phone,
            county=county,
            profile_pic=profile_pic,
            farm_name=farm_name,
            farming_type=farming_type,
            farm_size=float(farm_size or 0),
            experience=int(experience or 0),
            farm_description=farm_description,
            produce_categories=produce_categories_str,
            active_status=active_status,
            harvest_season=harvest_season,
            delivery=delivery,
        )
       

        login(request, user)

        return redirect("farmer_dashboard")

    return render(request, "farmer-register.html")


# =========================
# FARMER DASHBOARD
# =========================

# @login_required
# def farmer_dashboard(request):
#     profile = FarmerProfile.objects.get(user=request.user)
#     produce_list = Produce.objects.filter(farmer=profile).order_by('-created_at')
#     marketplace_list = Produce.objects.all().order_by('-created_at')
#     orders = Order.objects.filter(produce__farmer=profile).order_by('-created_at')
#
#     if request.method == 'POST':
#         name = request.POST.get('produceName')
#         quantity = request.POST.get('quantity')
#         price = request.POST.get('price')
#         image = request.FILES.get('image')
#
#         if name and quantity and price and image:
#             Produce.objects.create(
#                 farmer=profile,
#                 name=name,
#                 quantity=quantity,
#                 price=price,
#                 image=image
#             )
#             return redirect('farmer_dashboard')  # redirect to refresh listings
#
#     # Dashboard stats
#     total_listings = produce_list.count()
#     total_orders = 0  # you can calculate later when order model exists
#     total_income = sum([p.price * p.quantity for p in produce_list])
#
#     context = {
#         'produce_list': produce_list,
#         'marketplace_list': marketplace_list,
#         'total_listings': total_listings,
#         'total_orders': total_orders,
#         'total_income': total_income,
#     }
#
#     return render(request, 'myapp/farmer-dashboard.html', context)

# views.py
# from django.views.decorators.csrf import csrf_protect
#
# @csrf_protect
# @login_required
# def farmer_dashboard(request):
#     try:
#         profile = FarmerProfile.objects.get(user=request.user)
#     except ObjectDoesNotExist:
#         return redirect('farmer_register')
#
#     produce_list = Produce.objects.filter(farmer=profile).order_by('-created_at')
#     ## orders = Order.objects.filter(produce__farmer=profile).order_by('-created_at')
#
#     # ===========================
#     # AJAX Add Produce
#     # ===========================
#     # if request.method == 'POST' and request.headers.get('x-requested-with') == 'XMLHttpRequest':
#     #     name = request.POST.get('produceName')
#     #     quantity = request.POST.get('quantity')
#     #     price = request.POST.get('price')
#     #     image = request.FILES.get('image')
#     #
#     #     if not all([name, quantity, price, image]):
#     #         return JsonResponse({"success": False, "error": "All fields are required"})
#     #
#     #     produce = Produce.objects.create(
#     #         farmer=profile,
#     #         name=name,
#     #         quantity=float(quantity),
#     #         price=Decimal(price),
#     #         image=image,
#     #         status="Available"
#     #     )
#     #
#     #     return JsonResponse({
#     #         "success": True,
#     #         "produce": {
#     #             "id": produce.id,
#     #             "name": produce.name,
#     #             "price": str(produce.price),
#     #             "status": produce.status,
#     #             "image_url": produce.image.url,
#     #             "farmer_username": profile.user.username
#     #         }
#     #     })
#
#     # Dashboard stats
#     # total_listings = produce_list.count()
#     # total_orders = orders.count()
#     # total_income = sum([p.price * Decimal(p.quantity) for p in produce_list])
#
#     # context = {
#     #     'produce_list': produce_list,
#     #     'marketplace_list': marketplace_list,
#     #     'total_listings': total_listings,
#     #     'total_orders': total_orders,
#     #     'total_income': total_income,
#     #     'orders': orders
#     # }
#
#     # return render(request, 'farmer-dashboard.html', context)

# @login_required
# def farmer_dashboard(request):
#     try:
#         profile = FarmerProfile.objects.get(user=request.user)
#     except ObjectDoesNotExist:
#         return redirect("farmer_register")

#     if request.method == "POST":
#         name = request.POST.get("produceName")
#         quantity = request.POST.get("quantity")
#         price = request.POST.get("price")
#         image = request.FILES.get("image")

#         if name and quantity and price and image:
#             Produce.objects.create(
#                 farmer=profile,
#                 name=name,
#                 quantity=float(quantity),
#                 price=Decimal(price),
#                 image=image,
#                 status="Available",
#             )
#             return redirect("farmer_dashboard")

#     produce_list = Produce.objects.filter(farmer=profile).order_by("-created_at")
#     marketplace_list = Produce.objects.filter(status="Available").order_by("-created_at")
#     orders = OrderItem.objects.filter(
#         farmer=profile,
#         status__in=["Paid", "Delivery", "Completed"],
#     ).select_related("order", "produce", "order__buyer").order_by("-created_at")

#     total_listings = produce_list.count()
#     total_orders = orders.count()
#     total_income = sum(
#         [item.price for item in orders if item.status in ["Paid", "Delivery", "Completed"]],
#         Decimal("0.00"),
#     )

#     context = {
#         "produce_list": produce_list,
#         "marketplace_list": marketplace_list,
#         "orders": orders,
#         "total_listings": total_listings,
#         "total_orders": total_orders,
#         "total_income": total_income,
#         "wallet_balance": profile.balance,
#     }

#     return render(request, "farmer-dashboard.html", context)


# =========================
# MARKETPLACE
# =========================

# def marketplace(request):
#     produce_list = Produce.objects.filter(status="Available").order_by("-created_at")
#
#     context = {
#         "produce_list": produce_list
#     }
#
#     # return render(request, "marketplace.html", context)
#     return render(request, "marketplace.html", {"produce_list": produce_list})



@login_required
def farmer_dashboard(request):
    try:
        profile = FarmerProfile.objects.get(user=request.user)
    except ObjectDoesNotExist:
        return redirect("farmer_register")

    # ================= ADD PRODUCE (AJAX) =================
    if request.method == "POST":

        name = request.POST.get("produceName")
        quantity = request.POST.get("quantity")
        price = request.POST.get("price")
        image = request.FILES.get("image")

        if not all([name, quantity, price, image]):
            return JsonResponse({
                "success": False,
                "error": "All fields required"
            })

        produce = Produce.objects.create(
            farmer=profile,
            name=name,
            quantity=float(quantity),
            price=Decimal(price),
            image=image,
            status="Available",
        )

        return JsonResponse({
            "success": True,
            "produce": {
                "id": produce.id,
                "name": produce.name,
                "quantity": produce.quantity,
                "price": str(produce.price),
                "status": produce.status,
                "image_url": produce.image.url,
                "farmer_username": request.user.username,
            }
        })

    # ================= DASHBOARD DATA =================
    produce_list = Produce.objects.filter(
        farmer=profile
    ).order_by("-created_at")

    marketplace_list = Produce.objects.filter(
        status="Available"
    ).order_by("-created_at")
    

    orders = OrderItem.objects.filter(
        farmer=profile,
        status__in=["Paid", "Delivery", "Completed"],
    ).select_related(
        "order", "produce", "order__buyer"
    ).order_by("-created_at")

    total_listings = produce_list.count()
    total_orders = orders.count()

    total_income = sum(
        (item.price for item in orders),
        Decimal("0.00")
    )

    context = {
        "produce_list": produce_list,
        "marketplace_list": marketplace_list,
        "orders": orders,
        "total_listings": total_listings,
        "total_orders": total_orders,
        "total_income": total_income,
        "wallet_balance": profile.balance,
    }

    return render(request, "farmer-dashboard.html", context)
from django.shortcuts import render
from .models import Produce, Cart
@login_required
def marketplace(request):
    query = request.GET.get("q")
    category = request.GET.get("category")

    produce_list = Produce.objects.filter(status="Available")

    if query:
        produce_list = produce_list.filter(name__icontains=query)

    if category and category != "All":
        produce_list = produce_list.filter(name__icontains=category)

    produce_list = produce_list.order_by("-created_at")

    cart, created = Cart.objects.get_or_create(user=request.user)

    return render(request, "marketplace.html", {
        "produce_list": produce_list,
        "cart_count": cart.items.count(),
    })  

# =========================
# LEGACY ORDER VIEW (KEPT COMMENTED)
# =========================

# def create_order(request):
#
#     if request.method == "POST":
#
#         produce_id = request.POST.get("produce_id")
#         quantity = float(request.POST.get("quantity"))
#
#         buyer_name = request.POST.get("buyer_name")
#         buyer_phone = request.POST.get("buyer_phone")
#         buyer_location = request.POST.get("buyer_location")
#
#         produce = Produce.objects.get(id=produce_id)
#
#         total_price = produce.price * quantity
#
#         Order.objects.create(
#             produce=produce,
#             buyer_name=buyer_name,
#             buyer_phone=buyer_phone,
#             buyer_location=buyer_location,
#             quantity=quantity,
#             total_price=total_price
#         )
#
#         return JsonResponse({"success": True})
#
#     return JsonResponse({"success": False})

# def create_order(request):
#
#     if request.method == "POST":
#
#         produce_id = request.POST.get("produce_id")
#         quantity = Decimal(request.POST.get("quantity"))
#
#         buyer_name = request.POST.get("buyer_name")
#         buyer_phone = request.POST.get("buyer_phone")
#         buyer_location = request.POST.get("buyer_location")
#
#         produce = Produce.objects.get(id=produce_id)
#
#         total_price = produce.price * quantity
#
#         Order.objects.create(
#             produce=produce,
#             buyer_name=buyer_name,
#             buyer_phone=buyer_phone,
#             buyer_location=buyer_location,
#             quantity=quantity,
#             total_price=total_price
#         )
#
#         return JsonResponse({"success": True})
#
#     return JsonResponse({"success": False})


# =========================
# PRODUCE EDIT / DELETE
# =========================
@login_required
def edit_produce(request, produce_id):
    try:
        produce = Produce.objects.get(id=produce_id, farmer__user=request.user)
    except Produce.DoesNotExist:
        return JsonResponse({"success": False, "error": "Produce not found"})

    if request.method == "POST":
        name = request.POST.get("name")
        quantity = request.POST.get("quantity")
        price = request.POST.get("price")
        status = request.POST.get("status")
        image = request.FILES.get("image")

        if not (name and quantity and price and status):
            return JsonResponse({"success": False, "error": "All fields are required"})

        produce.name = name
        produce.quantity = quantity
        produce.price = price
        produce.status = status
        if image:
            produce.image = image
        produce.save()

        return JsonResponse(
            {
                "success": True,
                "produce": {
                    "id": produce.id,
                    "name": produce.name,
                    "quantity": produce.quantity,
                    "price": produce.price,
                    "status": produce.status,
                    "image_url": produce.image.url if produce.image else "",
                    "farmer_username": produce.farmer.user.username,
                },
            }
        )

    return JsonResponse({"success": False, "error": "Invalid request"})


@login_required
def delete_produce(request, produce_id):
    if request.method == "POST":
        try:
            produce = Produce.objects.get(id=produce_id, farmer__user=request.user)
            produce.delete()
            return JsonResponse({"success": True})
        except Produce.DoesNotExist:
            return JsonResponse({"success": False, "error": "Produce not found"})
    return JsonResponse({"success": False, "error": "Invalid request"})


# =========================
# BUYER REGISTER
# =========================
def buyer_register(request):
    if request.method == "POST":
        first_name = request.POST.get("firstName")
        last_name = request.POST.get("lastName")
        username = request.POST.get("username")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        county = request.POST.get("county")
        password = request.POST.get("password")

        if User.objects.filter(username=username).exists():
            return JsonResponse({"success": False, "error": "Username already exists"})

        user = User.objects.create_user(
            username=username,
            email=email,
            password=password,
            first_name=first_name,
            last_name=last_name,
        )

        login(request, user)

        return JsonResponse({"success": True, "redirect_url": "/buyer-dashboard/"})

    return render(request, "buyer-register.html")


# =========================
# BUYER DASHBOARD + CART + CHECKOUT
# =========================

@login_required
def buyer_dashboard(request):
    produce_list = Produce.objects.filter(status="Available").order_by("-created_at")
    orders = (
        Order.objects.filter(buyer=request.user)
        .prefetch_related("items", "items__produce", "items__farmer__user")
        .order_by("-created_at")
    )

    cart, created = Cart.objects.get_or_create(user=request.user)
    cart_count = cart.items.count()

    total_orders = orders.count()
    total_spent = sum([o.total_amount for o in orders], Decimal("0.00"))

    context = {
        "produce_list": produce_list,
        "orders": orders,
        "total_orders": total_orders,
        "total_spent": total_spent,
        "cart_count": cart_count,
    }

    return render(request, "buyer-dashboard.html", context)


@login_required
def add_to_cart(request, produce_id):
    if request.method == "POST":
        produce = Produce.objects.get(id=produce_id)
        cart, created = Cart.objects.get_or_create(user=request.user)

        cart_item, created = CartItem.objects.get_or_create(
            cart=cart,
            produce=produce,
            defaults={"quantity": 1},
        )

        if not created:
            cart_item.quantity += 1
            cart_item.save()

    return redirect(request.META.get("HTTP_REFERER", "buyer_dashboard"))


@login_required
def cart_view(request):
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart_items = cart.items.select_related("produce", "produce__farmer", "produce__farmer__user").all()

    cart_total = sum(
        [item.produce.price * Decimal(item.quantity) for item in cart_items],
        Decimal("0.00"),
    )

    context = {
        "cart": cart,
        "cart_items": cart_items,
        "cart_total": cart_total,
    }

    return render(request, "cart.html", context)


@login_required
def remove_from_cart(request, item_id):
    if request.method == "POST":
        cart = Cart.objects.get(user=request.user)
        item = CartItem.objects.get(id=item_id, cart=cart)
        item.delete()

    return redirect("cart_view")


@login_required
def checkout(request):
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart_items = cart.items.select_related("produce", "produce__farmer").all()

    if not cart_items.exists():
        messages.info(request, "Your cart is empty.")
        return redirect("cart_view")

    cart_total = sum(
        [item.produce.price * Decimal(item.quantity) for item in cart_items],
        Decimal("0.00"),
    )

    if request.method == "POST":
        phone = request.POST.get("phone")
        location = request.POST.get("location")

        order = Order.objects.create(
            buyer=request.user,
            phone=phone,
            location=location,
            delivery_fee=Decimal("0.00"),
            total_amount=cart_total,
            payment_status="Pending",
        )

        for item in cart_items:
            OrderItem.objects.create(
                order=order,
                produce=item.produce,
                farmer=item.produce.farmer,
                quantity=item.quantity,
                price=item.produce.price * Decimal(item.quantity),
                status="Pending",
            )

        cart.items.all().delete()
        messages.success(request, "Order placed successfully.")
        return redirect("buyer_dashboard")

    context = {
        "cart_items": cart_items,
        "cart_total": cart_total,
    }

    return render(request, "checkout.html", context)


# =========================
# ADVISOR REGISTER
# =========================
def advisor_register(request):
    if request.method == "POST":
        full_name = request.POST.get("fullName")
        username = request.POST.get("username")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        specialization = request.POST.get("specialization")
        bio = request.POST.get("bio")
        password = request.POST.get("password")

        if not username:
            return JsonResponse({"success": False, "error": "Username must be provided"})

        if User.objects.filter(username=username).exists():
            return JsonResponse({"success": False, "error": "Username already exists"})

        if User.objects.filter(email=email).exists():
            return JsonResponse({"success": False, "error": "Email already registered"})

        first_name = full_name.split()[0] if full_name else ""
        last_name = " ".join(full_name.split()[1:]) if full_name and len(full_name.split()) > 1 else ""

        user = User.objects.create_user(
            username=username,
            email=email,
            password=password,
            first_name=first_name,
            last_name=last_name,
        )

        AdvisorProfile.objects.create(
            user=user,
            phone=phone,
            specialization=specialization,
            bio=bio,
            status="Pending",
        )

        login(request, user)

        return JsonResponse(
            {"success": True, "message": "Registration submitted! Awaiting admin approval."}
        )

    return render(request, "advisor-register.html")


# =========================
# ADMIN - ADVISORS
# =========================
@staff_member_required
def pending_advisors(request):
    advisors = AdvisorProfile.objects.filter(status="Pending").order_by("-created_at")
    return render(request, "admin/pending-advisors.html", {"advisors": advisors})


@staff_member_required
def approve_advisor(request, advisor_id):
    advisor = AdvisorProfile.objects.get(id=advisor_id)
    advisor.status = "Approved"
    advisor.save()
    return redirect("admin_dashboard")


@staff_member_required
def reject_advisor(request, advisor_id):
    advisor = AdvisorProfile.objects.get(id=advisor_id)
    advisor.status = "Rejected"
    advisor.save()
    return redirect("admin_dashboard")


# pending_advisors
# from django.shortcuts import render
# from .models import AdvisorProfile  # or however you store advisor registrations
#
# def pending_advisors(request):
#     pending = AdvisorProfile.objects.filter(status='Pending')
#     context = {'pending_advisors': pending}
#     return render(request, 'pending_advisors.html', context)


# =========================
# ADMIN DASHBOARD
# =========================
@staff_member_required
def admin_dashboard(request):
    
    users = User.objects.all().order_by("-id")
    products = Produce.objects.all().order_by("-created_at")
    orders = (
        Order.objects.all()
        .prefetch_related("items", "items__produce", "items__farmer__user", "buyer")
        .order_by("-created_at")
    )

    total_revenue = sum([o.total_amount for o in orders if o.payment_status == "Paid"])
  
    advisors = AdvisorProfile.objects.filter(status="Pending").order_by("-created_at")
    pending_posts = AdvisorPost.objects.filter(status="Pending").order_by("-created_at")
    withdrawals = Withdrawal.objects.filter(status="Pending").select_related("farmer", "farmer__user")

    context = {
        "users": users,
        "products": products,
        "orders": orders,
        "advisors": advisors,
        "pending_posts": pending_posts,
        "withdrawals": withdrawals,
        "total_revenue": total_revenue,
        
    }

    return render(request, "admin-dashboard.html", context)


@staff_member_required
def suspend_user(request, user_id):
    user = get_object_or_404(User, id=user_id)
    user.is_active = False
    user.save()
    return redirect("admin_dashboard")


# =========================
# ADVISOR DASHBOARD / POSTS
# =========================

# advisor register view
@login_required
def advisor_dashboard(request):
    try:
        advisor = AdvisorProfile.objects.get(user=request.user)
    except AdvisorProfile.DoesNotExist:
        return redirect("login")

    if advisor.status != "Approved":
        return render(request, "advisor_pending.html", {"advisor": advisor})

    posts = AdvisorPost.objects.filter(advisor=advisor).order_by("-created_at")

    return render(
        request,
        "advisor-dashboard.html",
        {
            "advisor": advisor,
            "posts": posts,
        },
    )

# advisor posts view
@login_required
@csrf_protect
def create_advisor_post(request):
    if request.method == "POST":
        advisor = AdvisorProfile.objects.filter(user=request.user).first()

        if not advisor:
            return JsonResponse({"success": False, "error": "Not an advisor"})

        title = request.POST.get("title")
        category = request.POST.get("category")
        content = request.POST.get("content")
        image = request.FILES.get("image")

        if not all([title, category, content]):
            return JsonResponse({"success": False, "error": "All fields required"})

        AdvisorPost.objects.create(
            advisor=advisor,
            title=title,
            category=category,
            content=content,
            image=image,
            status="Pending",
        )

        return redirect("advisor_dashboard")

    return JsonResponse({"success": False})

# advisor-dashboard view
# from .models import AdvisorPost
#
# @login_required
# @ensure_csrf_cookie
# def advisor_dashboard(request):
#     try:
#         advisor = AdvisorProfile.objects.get(user=request.user)
#     except AdvisorProfile.DoesNotExist:
#         return redirect("login")
#
#     if advisor.status != "Approved":
#         return render(request, "advisor_pending.html", {"advisor": advisor})
#
#     # added this part
#     # if request.method == "POST":
#     #     title = request.POST.get("title")
#     #     category = request.POST.get("category")
#     #     content = request.POST.get("content")
#     #     image = request.FILES.get("image")
#     #     # Simple validation
#     #     if not all([title, category, content]):
#     #         messages.error(request, "Title, category, and content are required.")
#     #     else:
#     #
#     #         AdvisorPost.objects.create(
#     #             advisor=advisor,
#     #             title=title,
#     #             category=category,
#     #             content=content,
#     #             image=image,
#     #             status="Pending"
#     #         )
#
#     posts = AdvisorPost.objects.filter(advisor=advisor).order_by("-created_at")
#
#     return render(request, "advisor-dashboard.html", {
#         "advisor": advisor,
#         "posts": posts
#     })
#
#     # advisor login view
#     if AdvisorProfile.objects.filter(user=user).exists():
#         advisor = AdvisorProfile.objects.get(user=user)
#     if advisor.status == "Approved":
#         return redirect("advisor_dashboard")
#     else:
#         messages.info(request, "Your account is pending approval by admin.")
#         return redirect("login")


# =========================
# ADVISORY FEED
# =========================
@login_required
def advisory_feed(request):
    posts = AdvisorPost.objects.filter(status="Approved").order_by("-created_at")
    return render(request, "advisory-feed.html", {"posts": posts})


# =========================
# ADVISOR POST APPROVAL
# =========================
@staff_member_required
def pending_posts(request):
    return redirect("admin_dashboard")


@staff_member_required
def approve_post(request, post_id):
    post = AdvisorPost.objects.get(id=post_id)
    post.status = "Approved"
    post.save()
    return redirect("admin_dashboard")


@staff_member_required
def reject_post(request, post_id):
    post = AdvisorPost.objects.get(id=post_id)
    post.status = "Rejected"
    post.save()
    return redirect("admin_dashboard")


# =========================
# PAYMENTS / DELIVERY
# =========================

# admin confirm payment
# @staff_member_required
# def confirm_payment(request, order_id):
#     order = Order.objects.get(id=order_id)
#
#     order.payment_confirmed = True
#     order.status = "Paid"
#     order.save()
#
#     # Add money to farmer wallet
#     farmer = order.produce.farmer
#     farmer.balance += order.total_price
#     farmer.save()
#
#     return redirect("admin_dashboard")

# @login_required
# def checkout(request):
#     cart, created = Cart.objects.get_or_create(user=request.user)
#     cart_items = cart.items.select_related("produce", "produce__farmer").all()

#     if not cart_items.exists():
#         messages.info(request, "Your cart is empty.")
#         return redirect("cart_view")

#     items_total = sum(
#         [item.produce.price * Decimal(item.quantity) for item in cart_items],
#         Decimal("0.00"),
#     )

#     delivery_fee = items_total * Decimal("0.20")
#     total_amount = items_total + delivery_fee

#     if request.method == "POST":
#         phone = request.POST.get("phone")
#         location = request.POST.get("location")

#         order = Order.objects.create(
#             buyer=request.user,
#             phone=phone,
#             location=location,
#             delivery_fee=delivery_fee,
#             total_amount=total_amount,
#             payment_status="Pending",
#         )

#         for item in cart_items:
#             item_total = item.produce.price * Decimal(item.quantity)

#             OrderItem.objects.create(
#                 order=order,
#                 produce=item.produce,
#                 farmer=item.produce.farmer,
#                 quantity=item.quantity,
#                 price=item_total,
#                 status="Pending",
#             )

#         cart.items.all().delete()
#         messages.success(request, "Order placed successfully.")
#         return redirect("buyer_dashboard")

#     context = {
#         "cart_items": cart_items,
#         "items_total": items_total,
#         "delivery_fee": delivery_fee,
#         "cart_total": total_amount,
#     }

#     return render(request, "checkout.html", context)


#@staff_member_required
#def confirm_payment(request, order_id):
#    order = Order.objects.get(id=order_id)
#
 #   order.payment_status = "Paid"
  #  order.save()
#
 #   items = order.items.all()
#
 #   for item in items:
  #      item.status = "Paid"
   #     item.save()

    #    farmer = item.farmer
     #   farmer.balance += item.price
      #  farmer.save()

    #return redirect("admin_dashboard")



@staff_member_required
def confirm_payment(request, order_id):
    order = Order.objects.get(id=order_id)

    order.payment_status = "Paid"
    order.save()

    for item in order.items.all():
        item.status = "Paid"
        item.save()

    return redirect("admin_orders")



@staff_member_required
def start_delivery(request, order_id):
    order = Order.objects.get(id=order_id)

    for item in order.items.all():
        if item.status == "Paid":
            item.status = "Delivery"
            item.save()

    return redirect("admin_dashboard")


@login_required
def confirm_delivery(request, item_id):
    item = OrderItem.objects.get(id=item_id)

    if request.user != item.order.buyer:
        return redirect("buyer_dashboard")

    if item.status == "Delivery":
        item.status = "Completed"
        item.save()

        farmer = item.farmer
        payout = item.price + (item.price * Decimal("0.20"))
        farmer.balance += payout
        farmer.save()

    return redirect("buyer_dashboard")


# =========================
# WITHDRAWALS
# =========================
@login_required
def request_withdrawal(request):
    farmer = FarmerProfile.objects.get(user=request.user)

    if request.method == "POST":
        amount = Decimal(request.POST.get("amount"))

        if amount > farmer.balance:
            return JsonResponse({"error": "Insufficient balance"})

        Withdrawal.objects.create(farmer=farmer, amount=amount)
        return redirect("farmer_dashboard")

    return render(request, "withdraw.html")


@staff_member_required
def approve_withdrawal(request, withdrawal_id):
    withdrawal = Withdrawal.objects.get(id=withdrawal_id)
    farmer = withdrawal.farmer

    if farmer.balance >= withdrawal.amount:
        farmer.balance -= withdrawal.amount
        farmer.save()

        withdrawal.status = "Approved"
        withdrawal.save()

    return redirect("admin_dashboard")


@login_required
def wallet_view(request):
    farmer = FarmerProfile.objects.get(user=request.user)
    withdrawals = Withdrawal.objects.filter(farmer=farmer).order_by("-created_at")

    context = {
        "farmer": farmer,
        "withdrawals": withdrawals,
    }
    return render(request, "wallet.html", context)


@login_required
def request_withdrawal(request):
    farmer = FarmerProfile.objects.get(user=request.user)

    if request.method == "POST":
        amount = Decimal(request.POST.get("amount"))

        if amount <= 0:
            messages.error(request, "Enter a valid amount.")
            return redirect("wallet_view")

        if amount > farmer.balance:
            messages.error(request, "Insufficient balance.")
            return redirect("wallet_view")

        Withdrawal.objects.create(
            farmer=farmer,
            amount=amount,
            status="Pending"
        )

        messages.success(request, "Withdrawal request submitted.")
        return redirect("wallet_view")

    return redirect("wallet_view")


@staff_member_required
def approve_withdrawal(request, withdrawal_id):
    withdrawal = Withdrawal.objects.get(id=withdrawal_id)
    withdrawal.status = "Approved"
    withdrawal.save()
    return redirect("admin_dashboard")

# mark withdrawals view
@staff_member_required
def mark_withdrawal_paid(request, withdrawal_id):
    withdrawal = Withdrawal.objects.get(id=withdrawal_id)

    if withdrawal.status != "Approved":
        return redirect("admin_dashboard")

    farmer = withdrawal.farmer

    if farmer.balance >= withdrawal.amount:
        farmer.balance -= withdrawal.amount
        farmer.save()

        withdrawal.status = "Paid"
        withdrawal.save()

    return redirect("admin_dashboard")


@staff_member_required
def admin_withdrawals(request):
    withdrawals = Withdrawal.objects.select_related("farmer", "farmer__user").order_by("-created_at")

    context = {
        "withdrawals": withdrawals,
    }
    return render(request, "admin-withdrawals.html", context)


@staff_member_required
def approve_withdrawal(request, withdrawal_id):
    withdrawal = get_object_or_404(Withdrawal, id=withdrawal_id)

    if request.method == "POST" and withdrawal.status == "Pending":
        withdrawal.status = "Approved"
        withdrawal.save()

    return redirect("admin_withdrawals")


@staff_member_required
def mark_withdrawal_paid(request, withdrawal_id):
    withdrawal = get_object_or_404(Withdrawal, id=withdrawal_id)

    if request.method == "POST" and withdrawal.status == "Approved":
        farmer = withdrawal.farmer

        if farmer.balance >= withdrawal.amount:
            farmer.balance -= withdrawal.amount
            farmer.save()

            withdrawal.status = "Paid"
            withdrawal.save()

    return redirect("admin_withdrawals")

# admin orders view
@staff_member_required
def admin_orders(request):
    orders = (
        Order.objects.all()
        .prefetch_related("items", "items__produce", "items__farmer__user", "buyer")
        .order_by("-created_at")
    )

    context = {
        "orders": orders,
    }
    return render(request, "admin-orders.html", context)


@login_required
def farmer_orders(request):
    try:
        farmer = FarmerProfile.objects.get(user=request.user)
    except FarmerProfile.DoesNotExist:
        return redirect("farmer_register")

    orders = OrderItem.objects.filter(
        farmer=farmer
    ).select_related(
        "order", "produce", "order__buyer"
    ).order_by("-order__created_at")

    context = {
        "orders": orders
    }

    return render(request, "farmer-orders.html", context)


@login_required
def complete_delivery(request, item_id):
    item = OrderItem.objects.get(id=item_id)

    # Only farmer should do this
    if item.farmer.user != request.user:
        return redirect("farmer_orders")

    item.status = "Completed"
    item.save()

    return redirect("farmer_orders")


#farmer listings view 
@login_required
def farmer_listings(request):
    try:
        farmer = FarmerProfile.objects.get(user=request.user)
    except FarmerProfile.DoesNotExist:
        return redirect("farmer_register")

    if request.method == "POST":
        name = request.POST.get("produceName")
        quantity = request.POST.get("quantity")
        price = request.POST.get("price")
        image = request.FILES.get("image")

        if name and quantity and price and image:
            Produce.objects.create(
                farmer=farmer,
                name=name,
                quantity=float(quantity),
                price=Decimal(price),
                image=image,
                status="Available"
            )
            return redirect("farmer_listings")

    produce_list = Produce.objects.filter(farmer=farmer).order_by("-created_at")

    context = {
        "produce_list": produce_list,
    }
    return render(request, "farmer-listings.html", context)



@staff_member_required
def update_delivery_fee(request, order_id):
    order = Order.objects.get(id=order_id)

    if request.method == "POST":
        delivery_fee = Decimal(request.POST.get("delivery_fee", "0"))
        order.delivery_fee = delivery_fee

        items_total = sum([item.price for item in order.items.all()], Decimal("0.00"))
        order.total_amount = items_total + delivery_fee
        order.save()

    return redirect("admin_orders")




# import requests
# def checkout(request):
#     cart = Cart.objects.get(user=request.user)
#     cart_items = cart.items.all()
#     email = request.user.email
#     amount = int(total * Decimal("100"))  # Paystack uses kobo (×100)
#     phone=request.session.get("phone")
#     location=request.session.get("location")
#     items_total = sum(item.produce.price * item.quantity for item in cart_items)
#     delivery_fee = items_total * Decimal("0.20")
#     total = items_total + delivery_fee

#     if request.method == "POST":

#             request.session["phone"] = request.POST.get("phone")
#             request.session["location"] = request.POST.get("location")
        
      
        
#     location = request.session.get("location")
#     url = "https://api.paystack.co/transaction/initialize"
#     headers = {
#             "Authorization": f"Bearer {settings.PAYSTACK_SECRET_KEY}"
#         }
#     data = {
#             "email": email,
#             "amount": amount,
#             "callback_url": "http://127.0.0.1:8000/payment-success/"
#         }   
#     response = requests.post(url, headers=headers, json=data)
#     res_data = response.json()
        
#     if res_data["status"]:
#             return redirect(res_data["data"]["authorization_url"])
#         # if Order.objects.filter(payment_status="Paid", buyer=request.user).exists():
#        # prevent duplicate processing
#     return render(request, "checkout.html", {
#          "paystack_public_key": settings.PAYSTACK_PUBLIC_KEY,
#         "cart_items": cart_items,
#         "items_total": items_total,
#         "delivery_fee": delivery_fee,
#         "cart_total": total
       
#     })



@login_required
def checkout(request):
    cart = Cart.objects.get(user=request.user)
    cart_items = cart.items.all()

    items_total = sum(item.produce.price * item.quantity for item in cart_items)
    delivery_fee = items_total * Decimal("0.20")
    total = items_total + delivery_fee

    if request.method == "POST":
        # SAVE session FIRST
        request.session["phone"] = request.POST.get("phone")
        request.session["location"] = request.POST.get("location")

        email = request.user.email
        amount = int(total * 100)

        url = "https://api.paystack.co/transaction/initialize"
        headers = {
            "Authorization": f"Bearer {settings.PAYSTACK_SECRET_KEY}"
        }
        data = {
            "email": email,
            "amount": amount,
            "callback_url": "http://127.0.0.1:8000/verify-payment/"
        }

        response = requests.post(url, headers=headers, json=data)
        res_data = response.json()

        if res_data["status"]:
            return redirect(res_data["data"]["authorization_url"])

    return render(request, "checkout.html", {
        "cart_items": cart_items,
        "items_total": items_total,
        "delivery_fee": delivery_fee,
        "cart_total": total,
        "paystack_public_key": settings.PAYSTACK_PUBLIC_KEY
    })


def payment_success(request):
    reference = request.GET.get('reference')

    url = f"https://api.paystack.co/transaction/verify/{reference}"
    headers = {
        "Authorization": f"Bearer {settings.PAYSTACK_SECRET_KEY}"
    }

    response = requests.get(url, headers=headers)
    res_data = response.json()

    if res_data["status"] and res_data["data"]["status"] == "success":
        # Save order h
        cart = Cart.objects.get(user=request.user)
        cart.items.all().delete()

        return render(request, "success.html")

    return render(request, "failed.html")



def success_page(request):
    return render(request, "success.html")



import requests
from django.conf import settings
from django.shortcuts import redirect


# def verify_payment(request, ref):
#     url = f"https://api.paystack.co/transaction/verify/{ref}"
    
#     headers = {
#         "Authorization": f"Bearer {settings.PAYSTACK_SECRET_KEY}"
#     }

#     response = requests.get(url, headers=headers)
#     data = response.json()

#     if data["data"]["status"] == "success":
       
#         return redirect("success_page")

#     return render(request, "success.html", {
#     "ref": ref,
#     "amount": cart_total,
#     "items_total": items_total,
#     "delivery_fee": delivery_fee,
# })

from .models import Cart, CartItem, Order, OrderItem
import requests
from django.conf import settings
from django.shortcuts import render
from .models import Cart, Order, OrderItem

def verify_payment(request, ref):

    # verify payment
    url = f"https://api.paystack.co/transaction/verify/{ref}"
    headers = {
        "Authorization": f"Bearer {settings.PAYSTACK_SECRET_KEY}"
    }

    response = requests.get(url, headers=headers)
    data = response.json()

    if data["data"]["status"] == "success":

        cart, created = Cart.objects.get_or_create(user=request.user)
        cart_items = cart.items.all()

        #  calculate totals
        items_total = sum(item.produce.price * item.quantity for item in cart_items)
        delivery_fee = items_total * Decimal("0.2")
        total_amount = items_total + delivery_fee

        # create order
        order = Order.objects.create(
        buyer=request.user,
        phone=request.session.get("phone") or "N/A",
        location=request.session.get("location") or "N/A",
        delivery_fee=delivery_fee,
        total_amount=total_amount,
        payment_status="Paid",
        reference=ref
    )

        # create order items
        for item in cart_items:
            OrderItem.objects.create(
                order=order,
                produce=item.produce,
                farmer=item.produce.farmer,
                quantity=item.quantity,
                price=item.produce.price * item.quantity, 
                status="Paid"
            )

        # clear cart
        cart_items.delete()

        return render(request, "success.html", {
            "order": order,
            "ref": ref,
            "amount": total_amount,
            "items_total": items_total,
            "delivery_fee": delivery_fee,
        })
    if Order.objects.filter(reference=ref).exists():#prevent duplicate processing
     return redirect("success_page")

    return render(request, "payment_failed.html")



from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa

@login_required
def download_receipt(request, order_id):
    order = Order.objects.get(id=order_id, buyer=request.user)
    items = order.items.all()

    template = get_template("receipt.html")
    html = template.render({
        "order": order,
        "items": items
    })

    response = HttpResponse(content_type="application/pdf")
    response["Content-Disposition"] = f'attachment; filename="receipt_{order.id}.pdf"'

    pisa.CreatePDF(html, dest=response)

    return response


@staff_member_required
def admin_delete_product(request, product_id):
    product = get_object_or_404(Produce, id=product_id)

    if request.method == "POST":
        product.delete()

    return redirect("admin_dashboard")