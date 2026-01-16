""" 注册BaseDomain和SubDomain模型到admin站点 """

from django.contrib import admin
from domains.models import BaseDomain, SubDomain

admin.site.register(BaseDomain)
admin.site.register(SubDomain)
