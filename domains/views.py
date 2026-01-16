from django.shortcuts import render
from .models import SubDomain

def index(request):
    subdomains = SubDomain.objects.all()
    return render(request, "index.html", {"subdomains": subdomains})
