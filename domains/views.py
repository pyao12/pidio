""" Django视图管理 """

from django.shortcuts import render
from .models import SubDomain

def index(request):
    """ 域名管理首页 """
    subdomains = SubDomain.objects.all()
    return render(request, "index.html", {"subdomains": subdomains})
