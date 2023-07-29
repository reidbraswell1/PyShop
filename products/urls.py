from django.urls import path
from . import views

urlpatterns = [
    path('', views.products),
    path('new', views.new_products)
]