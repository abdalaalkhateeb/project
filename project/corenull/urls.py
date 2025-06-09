# core/urls.py

from django.urls import path
from .views import *

urlpatterns = [
    path('api/hotels/', hotel_list),
    path('api/restaurants/', restaurant_list),
    path('api/tours/', tour_list),
    path('api/attractions/', attraction_list),
    path('api/reviews/', review_list),
]
