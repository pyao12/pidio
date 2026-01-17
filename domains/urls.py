from django.urls import path
from .views import index, create_subdomain, edit_subdomain, delete_subdomain

urlpatterns = [
    path("", index, name="index"),
    path("create/", create_subdomain, name="create_subdomain"),
    path("edit/<int:pk>/", edit_subdomain, name="edit_subdomain"),
    path("delete/<int:pk>/", delete_subdomain, name="delete_subdomain"),
]
