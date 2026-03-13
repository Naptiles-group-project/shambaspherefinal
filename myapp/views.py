
# Create your views here.

from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import FarmerProfile
from django.contrib import messages
from django.contrib.auth import login
from django.http import JsonResponse



# home view
def home(request):
    return render(request,'index.html')

# farmer register view
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.http import JsonResponse
from .models import FarmerProfile

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


from .models import FarmerProfile, Produce
from django.contrib.auth.decorators import login_required

@login_required
def farmer_dashboard(request):
    profile = FarmerProfile.objects.get(user=request.user)
    produce_list = Produce.objects.filter(farmer=profile).order_by('-created_at')
    marketplace_list = Produce.objects.all().order_by('-created_at')

    if request.method == 'POST':
        name = request.POST.get('produceName')
        quantity = request.POST.get('quantity')
        price = request.POST.get('price')
        image = request.FILES.get('image')

        if name and quantity and price and image:
            Produce.objects.create(
                farmer=profile,
                name=name,
                quantity=quantity,
                price=price,
                image=image
            )
            return redirect('farmer_dashboard')  # redirect to refresh listings

    # Dashboard stats
    total_listings = produce_list.count()
    total_orders = 0  # you can calculate later when order model exists
    total_income = sum([p.price * p.quantity for p in produce_list])

    context = {
        'produce_list': produce_list,
        'marketplace_list': marketplace_list,
        'total_listings': total_listings,
        'total_orders': total_orders,
        'total_income': total_income,
    }

    return render(request, 'myapp/farmer-dashboard.html', context)



from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from .models import FarmerProfile, Produce

@login_required
def farmer_dashboard(request):
    try:
        profile = FarmerProfile.objects.get(user=request.user)
    except ObjectDoesNotExist:
        # Redirect users who don't have a farmer profile
        return redirect('farmer_register')

    produce_list = Produce.objects.filter(farmer=profile).order_by('-created_at')
    marketplace_list = Produce.objects.all().order_by('-created_at')

    if request.method == 'POST':
        name = request.POST.get('produceName')
        quantity = request.POST.get('quantity')
        price = request.POST.get('price')
        image = request.FILES.get('image')

        if name and quantity and price and image:
            Produce.objects.create(
                farmer=profile,
                name=name,
                quantity=quantity,
                price=price,
                image=image
            )
            return redirect('farmer_dashboard')  # refresh listings

    # Dashboard stats
    total_listings = produce_list.count()
    total_orders = 0  # can calculate once you add orders
    total_income = sum([p.price * p.quantity for p in produce_list])

    context = {
        'produce_list': produce_list,
        'marketplace_list': marketplace_list,
        'total_listings': total_listings,
        'total_orders': total_orders,
        'total_income': total_income,
    }

    return render(request, 'farmer-dashboard.html', context)

# marketplace view
def marketplace(request):
    produce_list = Produce.objects.filter(status='Available').order_by('-created_at')
    return render(request, 'marketplace.html', {'produce_list': produce_list})
