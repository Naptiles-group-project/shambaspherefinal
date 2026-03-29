from django.shortcuts import render
from .models import AdvisorProfile, AdvisorPost

def pending_advisors(request):
    advisors = AdvisorProfile.objects.filter(status="Pending")
    return render(request, "admin/pending_advisors.html", {"advisors": advisors})


def pending_posts(request):
    posts = AdvisorPost.objects.filter(status="Pending")
    return render(request, "admin/pending_posts.html", {"posts": posts})