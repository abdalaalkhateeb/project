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
    
class HotelRoomsView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, hotel_id):
        hotel = get_object_or_404(Hotel, pk=hotel_id)  # تأكد أن الفندق موجود

        rooms = Room.objects.filter(hotel=hotel)  # جلب الغرف المرتبطة بالفندق

        serializer = RoomDetailSerializer(rooms, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class RoomsList(APIView):
    permission_classes = [IsAuthenticated]  

    def get(self, request):
        rooms = Room.objects.all()
        serializer = RoomDetailSerializer(rooms, many=True)
        return Response(serializer.data)


# class Hotels(APIView):
#     permission_classes = [IsAuthenticated]

#     def get(self, request):
#         hotels = Hotel.objects.all()
#         filterset = HotelFilter(request.query_params, queryset=hotels)
#         if filterset.is_valid():
#             serializer = HotelSerializer(filterset.qs, many=True)
#             return Response(serializer.data)
#         return Response(filterset.errors, status=status.HTTP_400_BAD_REQUEST)

# class HotelRoomsView(APIView):
#     permission_classes = [IsAuthenticated]

#     def get(self, request, hotel_id):
#         hotel = get_object_or_404(Hotel, pk=hotel_id)
#         rooms = Room.objects.filter(hotel=hotel)
#         filterset = RoomFilter(request.query_params, queryset=rooms)
#         if filterset.is_valid():
#             serializer = RoomDetailSerializer(filterset.qs, many=True)
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         return Response(filterset.errors, status=status.HTTP_400_BAD_REQUEST)

# class RoomsList(APIView):
#     permission_classes = [IsAuthenticated]

#     def get(self, request):
#         rooms = Room.objects.all()
#         filterset = RoomFilter(request.query_params, queryset=rooms)
#         if filterset.is_valid():
#             serializer = RoomDetailSerializer(filterset.qs, many=True)
#             return Response(serializer.data)
#         return Response(filterset.errors, status=status.HTTP_400_BAD_REQUEST)
# class RoomDetail(APIView):
#     permission_classes = [IsAuthenticated]

#     def get(self, request, pk):
#         room = get_object_or_404(Room, pk=pk)
#         serializer = RoomDetailSerializer(room)
#         return Response(serializer.data)