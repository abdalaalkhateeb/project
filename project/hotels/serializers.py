from rest_framework import serializers
from core.models import Hotel, Room

class HotelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Hotel
        fields = "__all__"


class RoomDetailSerializer(serializers.ModelSerializer):
    hotel = HotelSerializer()
    class Meta:
        model = Room
        fields = "__all__"
