# core/urls.py

from django.urls import path

from .views import contact_us

urlpatterns = [
    path('contact/', contact_us, name='contact_us'),
]
