from rest_framework import serializers
from core.models import Hotel, Room

class HotelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hotel
        fields = ['hotel_id', 'name', 'location', 'rating', 'price_range', 'contact_info', 'available_rooms', 'description']

class RoomDetailSerializer(serializers.ModelSerializer):
    hotel = HotelSerializer()  # تضمين تفاصيل الفندق المرتبط

    class Meta:
        model = Room
        fields = ['room_id', 'hotel', 'room_type', 'price_per_night', 'availability', 'capacity', 'description']
