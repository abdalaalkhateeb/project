from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import HotelSerializer, RoomDetailSerializer
from core.models import Hotel, Room
from rest_framework import status
from rest_framework.permissions import IsAuthenticated 
from rest_framework.generics import get_object_or_404


class Hotels(APIView):
    permission_classes = [IsAuthenticated]  

    def get(self, request):
        hotels = Hotel.objects.all()
        serializer = HotelSerializer(hotels, many=True)
        return Response(serializer.data)

class RoomsList(APIView):
    permission_classes = [IsAuthenticated]  

    def get(self, request):
        rooms = Room.objects.all()
        serializer = RoomDetailSerializer(rooms, many=True)
        return Response(serializer.data)

class RoomDetail(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        room = get_object_or_404(Room, pk=pk)
        serializer = RoomDetailSerializer(room)
        return Response(serializer.data)