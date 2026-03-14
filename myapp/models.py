from django.db import models
from django.contrib.auth.models import User


# Farmer Profile
class FarmerProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    # Contact & Personal
    phone = models.CharField(max_length=20)
    county = models.CharField(max_length=100)
    profile_pic = models.ImageField(upload_to='profiles/', blank=True, null=True)
    
    # Farm Info
    farm_name = models.CharField(max_length=200)
    farming_type = models.CharField(max_length=100)
    farm_size = models.FloatField()
    experience = models.IntegerField()
    farm_description = models.TextField(blank=True)
    
    # Produce Categories
    produce_categories = models.CharField(max_length=255, blank=True)  # comma-separated
    
    # Availability
    active_status = models.CharField(max_length=10)
    harvest_season = models.CharField(max_length=50)
    delivery = models.CharField(max_length=10)

    def __str__(self):
        return self.user.username


# Produce model
class Produce(models.Model):
    farmer = models.ForeignKey(FarmerProfile, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    quantity = models.FloatField()  # in kg
    price = models.DecimalField(max_digits=10, decimal_places=2)  # in KSh
    image = models.ImageField(upload_to='produce_images/')
    status = models.CharField(max_length=20, default='Available')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.farmer.user.username}"



# Order model
class Order(models.Model):
    produce = models.ForeignKey(Produce, on_delete=models.CASCADE)
    buyer_name = models.CharField(max_length=100)
    buyer_phone = models.CharField(max_length=20)
    buyer_location = models.CharField(max_length=200)

    quantity = models.FloatField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)

    status = models.CharField(
        max_length=20,
        default="Pending",
        choices=[
            ("Pending", "Pending"),
            ("Accepted", "Accepted"),
            ("Delivered", "Delivered")
        ]
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.produce.name} order by {self.buyer_name}"
