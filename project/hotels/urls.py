# hotels/urls.py

from django.urls import path
from .views import Hotels , RoomsList, RoomDetail

urlpatterns = [
    path('', Hotels.as_view(), name='all-hotels'),
    path('Rooms/', RoomsList.as_view(), name='all-rooms'),
    path('Room/<int:pk>/', RoomDetail.as_view(), name='room-detail'),
]

# This file defines the URL patterns for the Hotels app, mapping URLs to views.