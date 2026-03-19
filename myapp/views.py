from django.views.decorators.csrf import ensure_csrf_cookie, csrf_protect
from django.views.decorators.csrf import ensure_csrf_cookie
# Create your views here.

from django.shortcuts import render, redirect
from django.contrib.auth.models import User
# from requests import request
from .models import FarmerProfile
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.http import JsonResponse
from .models import FarmerProfile, Produce, Order

from .models import FarmerProfile, Produce
from .models import AdvisorProfile
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from .models import FarmerProfile, Produce
from decimal import Decimal
from .models import AdvisorPost



# home view
def home(request):
    return render(request,'index.html')

# login view
from django.contrib.auth import authenticate, login as auth_login

from django.contrib import messages
# from .models import FarmerProfile
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.models import User
from django.contrib import messages
from .models import FarmerProfile
# AdvisorProfile  # assuming you have a model for advisors

# def login_view(request):
#     if request.method == "POST":
#         username = request.POST.get("username")
#         password = request.POST.get("password")

#         user = authenticate(request, username=username, password=password)

#         if user is not None:
#             auth_login(request, user)

#             if user.is_superuser:
#                 return redirect("/admin/")

#             if FarmerProfile.objects.filter(user=user).exists():
#                 return redirect("farmer_dashboard")

#             # Add other roles like AdvisorProfile if needed
#             # if AdvisorProfile.objects.filter(user=user).exists():
#             #     return redirect("advisor_dashboard")

#             # Default: Buyer
#             return redirect("marketplace")

#         else:
#             messages.error(request, "Invalid username or password")

#     return render(request, "login.html")

# logout view
from django.contrib.auth import logout as auth_logout
def logout_view(request):
    auth_logout(request)
    return redirect('login')


# farmer register view


# def farmer_register(request):
#     if request.method == "POST":
#         # Personal Info
#         first_name = request.POST.get("firstName")
#         last_name = request.POST.get("lastName")
#         username = request.POST.get("username")
#         email = request.POST.get("email")
#         phone = request.POST.get("phone")
#         county = request.POST.get("county")

#         # Farm Info
#         farm_name = request.POST.get("farmName")
#         farming_type = request.POST.get("farmingType")
#         farm_size = request.POST.get("farmSize")
#         experience = request.POST.get("experience")
#         farm_description = request.POST.get("farmDescription")

#         # Produce Categories (checkboxes)
#         produce_categories = request.POST.getlist("produceCategories")
#         produce_categories_str = ",".join(produce_categories)

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

#         # Farm Info
#         farm_name = request.POST.get("farmName")
#         farming_type = request.POST.get("farmingType")
#         farm_size = request.POST.get("farmSize")
#         experience = request.POST.get("experience")
#         farm_description = request.POST.get("farmDescription")

#         # Produce Categories (checkboxes)
#         produce_categories = request.POST.getlist("produceCategories")
#         produce_categories_str = ",".join(produce_categories)

#         # Availability & Security
#         active_status = request.POST.get("activeStatus")
#         harvest_season = request.POST.get("harvestSeason")
#         delivery = request.POST.get("delivery")
#         password = request.POST.get("password")

#         # Profile Picture
#         profile_pic = request.FILES.get("profilePic")

#         # Check username
#         if User.objects.filter(username=username).exists():
#             return JsonResponse({"success": False, "error": "Username already exists"})

#         # Create user
#         user = User.objects.create_user(
#             username=username,
#             email=email,
#             password=password,
#             first_name=first_name,
#             last_name=last_name
#         )

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

#         # Auto-login
#         login(request, user)

#         return JsonResponse({"success": True, "redirect_url": "/farmer-dashboard/"})

#     return render(request, "farmer-register.html")





from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import FarmerProfile
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.http import JsonResponse
from .models import FarmerProfile, Produce, Order

from .models import FarmerProfile, Produce
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from .models import FarmerProfile, Produce






# login view

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
            
            # Add other roles like AdvisorProfile 
            if AdvisorProfile.objects.filter(user=user).exists():
                return redirect("advisor_dashboard")

            return redirect("buyer_dashboard")

            

            # Default: Buyer
            return redirect("marketplace")

        else:
            messages.error(request, "Invalid username or password")

    return render(request, "login.html")

# logout view
from django.contrib.auth import logout as auth_logout
def logout_view(request):
    auth_logout(request)
    return redirect('login')


# farmer register view


# def farmer_register(request):
#     if request.method == "POST":
#         # Personal Info
#         first_name = request.POST.get("firstName")
#         last_name = request.POST.get("lastName")
#         username = request.POST.get("username")
#         email = request.POST.get("email")
#         phone = request.POST.get("phone")
#         county = request.POST.get("county")

#         # Farm Info
#         farm_name = request.POST.get("farmName")
#         farming_type = request.POST.get("farmingType")
#         farm_size = request.POST.get("farmSize")
#         experience = request.POST.get("experience")
#         farm_description = request.POST.get("farmDescription")

#         # Produce Categories (checkboxes)
#         produce_categories = request.POST.getlist("produceCategories")
#         produce_categories_str = ",".join(produce_categories)

#         # Availability & Security
#         active_status = request.POST.get("activeStatus")


def farmer_register(request):
    if request.method == "POST":
        # Personal Info
        first_name = request.POST.get("firstName")
        last_name = request.POST.get("lastName")
        username = request.POST.get("username")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        county = request.POST.get("county")

        # Farm Info
        farm_name = request.POST.get("farmName")
        farming_type = request.POST.get("farmingType")
        farm_size = request.POST.get("farmSize")
        experience = request.POST.get("experience")
        farm_description = request.POST.get("farmDescription")

        # Produce Categories (checkboxes)
        produce_categories = request.POST.getlist("produceCategories")
        produce_categories_str = ",".join(produce_categories)

        # Availability & Security
        active_status = request.POST.get("activeStatus")
        harvest_season = request.POST.get("harvestSeason")
        delivery = request.POST.get("delivery")
        password = request.POST.get("password")

        # Profile Picture
        profile_pic = request.FILES.get("profilePic")

        # Check username
        if User.objects.filter(username=username).exists():
            return JsonResponse({"success": False, "error": "Username already exists"})

        # Create user
        user = User.objects.create_user(
            username=username,
            email=email,
            password=password,
            first_name=first_name,
            last_name=last_name
        )

        # Create FarmerProfile
        FarmerProfile.objects.create(
            user=user,
            phone=phone,
            county=county,
            profile_pic=profile_pic,
            farm_name=farm_name,
            farming_type=farming_type,
            farm_size=float(farm_size) if farm_size else 0,
            experience=int(experience) if experience else 0,
            farm_description=farm_description,
            produce_categories=produce_categories_str,
            active_status=active_status,
            harvest_season=harvest_season,
            delivery=delivery
        )

        # Auto-login
        login(request, user)

        return JsonResponse({"success": True, "redirect_url": "/farmer-dashboard/"})

    return render(request, "farmer-register.html")

# farmerDashboard views



# @login_required
# def farmer_dashboard(request):
#     profile = FarmerProfile.objects.get(user=request.user)
#     produce_list = Produce.objects.filter(farmer=profile).order_by('-created_at')
#     marketplace_list = Produce.objects.all().order_by('-created_at')
#     orders = Order.objects.filter(produce__farmer=profile).order_by('-created_at')

#     if request.method == 'POST':
#         name = request.POST.get('produceName')
#         quantity = request.POST.get('quantity')
#         price = request.POST.get('price')
#         image = request.FILES.get('image')

#         if name and quantity and price and image:
#             Produce.objects.create(
#                 farmer=profile,
#                 name=name,
#                 quantity=quantity,
#                 price=price,
#                 image=image
#             )
#             return redirect('farmer_dashboard')  # redirect to refresh listings

#     # Dashboard stats
#     total_listings = produce_list.count()
#     total_orders = 0  # you can calculate later when order model exists
#     total_income = sum([p.price * p.quantity for p in produce_list])

#     context = {
#         'produce_list': produce_list,
#         'marketplace_list': marketplace_list,
#         'total_listings': total_listings,
#         'total_orders': total_orders,
#         'total_income': total_income,
#     }

#     return render(request, 'myapp/farmer-dashboard.html', context)

#farmer dashboard view with AJAX support for adding produce without page refresh

# views.py

@login_required
def farmer_dashboard(request):
    try:
        profile = FarmerProfile.objects.get(user=request.user)
    except ObjectDoesNotExist:
        return redirect('farmer_register')

    produce_list = Produce.objects.filter(farmer=profile).order_by('-created_at')
    marketplace_list = Produce.objects.filter(status="Available").order_by('-created_at')
    orders = Order.objects.filter(produce__farmer=profile).order_by('-created_at')

    # ===========================
    # AJAX Add Produce
    # ===========================
    if request.method == 'POST' and request.headers.get('x-requested-with') == 'XMLHttpRequest':
        name = request.POST.get('produceName')
        quantity = request.POST.get('quantity')
        price = request.POST.get('price')
        image = request.FILES.get('image')

        if not all([name, quantity, price, image]):
            return JsonResponse({"success": False, "error": "All fields are required"})

        produce = Produce.objects.create(
            farmer=profile,
            name=name,
            quantity=float(quantity),
            price=Decimal(price),
            image=image,
            status="Available"
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
                "farmer_username": profile.user.username
            }
        })

    # Dashboard stats
    total_listings = produce_list.count()
    total_orders = orders.count()
    total_income = sum([p.price * Decimal(p.quantity) for p in produce_list])

    context = {
        'produce_list': produce_list,
        'marketplace_list': marketplace_list,
        'total_listings': total_listings,
        'total_orders': total_orders,
        'total_income': total_income,
        'orders': orders
    }

    return render(request, 'farmer-dashboard.html', context)
# marketplace view


# def marketplace(request):
#     produce_list = Produce.objects.filter(status="Available").order_by("-created_at")

#     context = {
#         "produce_list": produce_list
#     }

#     # return render(request, "marketplace.html", context)
    
#     return render(request, "marketplace.html", {"produce_list": produce_list})




# order view
from .models import Produce, Order
from django.http import JsonResponse


def create_order(request):

    if request.method == "POST":

        produce_id = request.POST.get("produce_id")
        quantity = float(request.POST.get("quantity"))

        buyer_name = request.POST.get("buyer_name")
        buyer_phone = request.POST.get("buyer_phone")
        buyer_location = request.POST.get("buyer_location")

        produce = Produce.objects.get(id=produce_id)

        total_price = produce.price * quantity

        Order.objects.create(
            produce=produce,
            buyer_name=buyer_name,
            buyer_phone=buyer_phone,
            buyer_location=buyer_location,
            quantity=quantity,
            total_price=total_price
        )

        return JsonResponse({"success": True})

    return JsonResponse({"success": False})



# marketplace view


def marketplace(request):
    produce_list = Produce.objects.filter(status="Available").order_by("-created_at")

    context = {
        "produce_list": produce_list
    }

    return render(request, "marketplace.html", context)




# order view
from .models import Produce, Order
from django.http import JsonResponse


def create_order(request):

    if request.method == "POST":

        produce_id = request.POST.get("produce_id")
        quantity = float(request.POST.get("quantity"))

        buyer_name = request.POST.get("buyer_name")
        buyer_phone = request.POST.get("buyer_phone")
        buyer_location = request.POST.get("buyer_location")

        produce = Produce.objects.get(id=produce_id)

        total_price = produce.price * quantity

        Order.objects.create(
            produce=produce,
            buyer_name=buyer_name,
            buyer_phone=buyer_phone,
            buyer_location=buyer_location,
            quantity=quantity,
            total_price=total_price
        )

        return JsonResponse({"success": True})

    return JsonResponse({"success": False})

# edit produce view
@login_required
def edit_produce(request, produce_id):
    try:
        produce = Produce.objects.get(id=produce_id, farmer__user=request.user)
    except Produce.DoesNotExist:
        return JsonResponse({'success': False, 'error': 'Produce not found'})

    if request.method == 'POST':
        name = request.POST.get('name')
        quantity = request.POST.get('quantity')
        price = request.POST.get('price')
        status = request.POST.get('status')
        image = request.FILES.get('image')

        if not (name and quantity and price and status):
            return JsonResponse({'success': False, 'error': 'All fields are required'})

        produce.name = name
        produce.quantity = quantity
        produce.price = price
        produce.status = status
        if image:
            produce.image = image
        produce.save()

        return JsonResponse({
            'success': True,
            'produce': {
                'id': produce.id,
                'name': produce.name,
                'quantity': produce.quantity,
                'price': produce.price,
                'status': produce.status,
                'image_url': produce.image.url if produce.image else '',
                'farmer_username': produce.farmer.user.username
            }
        })

    return JsonResponse({'success': False, 'error': 'Invalid request'})


# delete produce view
@login_required
def delete_produce(request, produce_id):
    if request.method == 'POST':
        try:
            produce = Produce.objects.get(id=produce_id, farmer__user=request.user)
            produce.delete()
            return JsonResponse({'success': True})
        except Produce.DoesNotExist:
            return JsonResponse({'success': False, 'error': 'Produce not found'})
    return JsonResponse({'success': False, 'error': 'Invalid request'})


# # buyer register
def buyer_register(request):

    if request.method == "POST":
      
        first_name = request.POST.get("firstName")
        last_name = request.POST.get("lastName")
        username = request.POST.get("username")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        county = request.POST.get("county")
        password = request.POST.get("password")

        # check if username exists
        if User.objects.filter(username=username).exists():
            return JsonResponse({
                "success": False,
                "error": "Username already exists"
            })

        # create user
        user = User.objects.create_user(
            username=username,
            email=email,
            password=password,
            first_name=first_name,
            last_name=last_name
        )

        # auto login
        login(request, user)

        return JsonResponse({
            "success": True,
            "redirect_url": "/buyer-dashboard/"
        })

    return render(request, "buyer-register.html")





from django.contrib.auth.models import User
from django.contrib.auth import login
from django.http import JsonResponse
from .models import AdvisorProfile
from django.shortcuts import render

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

        # Create user
        user = User.objects.create_user(
            username=username,
            email=email,
            password=password,
            first_name=first_name,
            last_name=last_name
        )

        # Create advisor profile
        AdvisorProfile.objects.create(
            user=user,
            phone=phone,
            specialization=specialization,
            bio=bio,
            status="Pending"
        )

        login(request, user)

        return JsonResponse({
            "success": True,
            "message": "Registration submitted! Awaiting admin approval."
        })

    return render(request, "advisor-register.html")

# buyer dashboard view
from django.contrib.auth.decorators import login_required
from .models import Produce, Order

@login_required
def buyer_dashboard(request):

    produce_list = Produce.objects.filter(status="Available")

    orders = Order.objects.filter(buyer_name=request.user.username)

    total_orders = orders.count()

    total_spent = sum([o.total_price for o in orders])

    context = {
        "produce_list": produce_list,
        "orders": orders,
        "total_orders": total_orders,
        "total_spent": total_spent
    }

    return render(request, "buyer-dashboard.html", context)


from django.contrib.admin.views.decorators import staff_member_required

# List pending advisors
@staff_member_required
def pending_advisors(request):
    advisors = AdvisorProfile.objects.filter(status="Pending").order_by("-created_at")
    return render(request, "admin/pending-advisors.html", {"advisors": advisors})

# Approve advisor
@staff_member_required
def approve_advisor(request, advisor_id):
    try:
        advisor = AdvisorProfile.objects.get(id=advisor_id)
        advisor.status = "Approved"
        advisor.save()
        return JsonResponse({"success": True, "status": advisor.status})
    except AdvisorProfile.DoesNotExist:
        return JsonResponse({"success": False, "error": "Advisor not found"})

# Reject advisor
@staff_member_required
def reject_advisor(request, advisor_id):
    try:
        advisor = AdvisorProfile.objects.get(id=advisor_id)
        advisor.status = "Rejected"
        advisor.save()
        return JsonResponse({"success": True, "status": advisor.status})
    except AdvisorProfile.DoesNotExist:
        return JsonResponse({"success": False, "error": "Advisor not found"})
    


# pending_advisors
from django.shortcuts import render
from .models import AdvisorProfile  # or however you store advisor registrations

def pending_advisors(request):
    pending = AdvisorProfile.objects.filter(status='Pending')
    context = {'pending_advisors': pending}
    return render(request, 'pending_advisors.html', context)





# admin-dash view
from django.contrib.admin.views.decorators import staff_member_required


@staff_member_required
def admin_dashboard(request):

    users = User.objects.all()
    products = Produce.objects.all()
    orders = Order.objects.all()
    advisors = AdvisorProfile.objects.filter(status="Pending")
    pending_posts = AdvisorPost.objects.filter(status="Pending").order_by("-created_at")  # <-- new


    context = {
        "users": users,
        "products": products,
        "orders": orders,
        "advisors": advisors,
        "pending_posts": pending_posts
    }

    return render(request, "admin-dashboard.html", context)


# suspend user
from django.shortcuts import get_object_or_404

@staff_member_required
def suspend_user(request, user_id):

    user = get_object_or_404(User, id=user_id)

    user.is_active = False
    user.save()

    return redirect("admin_dashboard")


# approve.reject advisor views
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

   #advisor register view
@login_required
def advisor_dashboard(request):

    advisor = AdvisorProfile.objects.get(user=request.user)

    context = {
        "advisor": advisor
    }

    return render(request, "advisor-dashboard.html", context)

#advisor posts view
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

        post = AdvisorPost.objects.create(
            advisor=advisor,
            title=title,
            category=category,
            content=content,
            image=image,
            status="Pending", 
        )

        return JsonResponse({
            "success": True,
            "post": {
                "id": post.id,
                "title": post.title,
                "category": post.category,
                "content": post.content
            }
        })

    return JsonResponse({"success": False})

#advisor-dashboard view
from .models import AdvisorPost

@login_required
@ensure_csrf_cookie
def advisor_dashboard(request):
    try:
        advisor = AdvisorProfile.objects.get(user=request.user)
    except AdvisorProfile.DoesNotExist:
        return redirect("login")

    if advisor.status != "Approved":
        return render(request, "advisor_pending.html", {"advisor": advisor})
    

    #added this part
    #if request.method == "POST":
        #title = request.POST.get("title")
        #category = request.POST.get("category")
        #content = request.POST.get("content")
        #image = request.FILES.get("image")
         # Simple validation
        #if not all([title, category, content]):
           # messages.error(request, "Title, category, and content are required.")
        #else:

            #AdvisorPost.objects.create(
            #advisor=advisor,
            #title=title,
            #category=category,
            #content=content,
            #image=image,
            #status="Pending"
    #)

    posts = AdvisorPost.objects.filter(advisor=advisor).order_by("-created_at")

    return render(request, "advisor-dashboard.html", {
        "advisor": advisor,
        "posts": posts
    })
     
     
     #advisor login view
    if AdvisorProfile.objects.filter(user=user).exists():
        advisor = AdvisorProfile.objects.get(user=user)
    if advisor.status == "Approved":
        return redirect("advisor_dashboard")
    else:
        messages.info(request, "Your account is pending approval by admin.")
        return redirect("login")
    
    
    #advisory page view
@login_required
def advisory_feed(request):
        posts = AdvisorPost.objects.filter(status="Approved").order_by("-created_at")

        return render(request, "advisory-feed.html", {
        "posts": posts
    })


    #admin advisory post approval view
from django.contrib.admin.views.decorators import staff_member_required

@staff_member_required
def pending_posts(request):
    # Redirect to admin dashboard where pending posts section already exists
    return redirect("admin_dashboard")

    #approve advisory post view
@staff_member_required
def approve_post(request, post_id):
    post = AdvisorPost.objects.get(id=post_id)
    post.status = "Approved"
    post.save()
    return redirect("admin_dashboard")  # redirect to dashboard
    
    
    #reject advisory post view
@staff_member_required
def reject_post(request, post_id):
    post = AdvisorPost.objects.get(id=post_id)
    post.status = "Rejected"
    post.save()
    return redirect("admin_dashboard")  # redirect to dashboard


#create_advisor_post
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

        post = AdvisorPost.objects.create(
            advisor=advisor,
            title=title,
            category=category,
            content=content,
            image=image,
            status="Pending",
        )

       # return JsonResponse({"success": True})
        return redirect("advisor_dashboard")

    return JsonResponse({"success": False})

 
