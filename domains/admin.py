from django.contrib import admin
from domains.models import BaseDomain, SubDomain

admin.site.register(BaseDomain)
admin.site.register(SubDomain)
