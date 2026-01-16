""" 域名管理相关URL配置 """

from django.urls import path
from .views import index

urlpatterns = [
    path("", index, name="index"),
]
