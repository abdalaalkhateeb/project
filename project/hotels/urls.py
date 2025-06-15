# hotels/urls.py

from django.urls import path
from .views import Hotels , RoomsList, HotelRoomsView

urlpatterns = [
    path('', Hotels.as_view(), name='all-hotels'),
    path('rooms/', RoomsList.as_view(), name='all-rooms'),
    # path('rooms/<int:pk>/', RoomDetail.as_view(), name='room-detail'),
     path("<int:hotel_id>/rooms/", HotelRoomsView.as_view(), name="hotel-rooms"),
]

# This file defines the URL patterns for the Hotels app, mapping URLs to views.