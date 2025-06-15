from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from core.models import Restaurant
from .serializers import RestaurantSerializer

class RestaurantList(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        restaurants = Restaurant.objects.using('external').all()
        serializer = RestaurantSerializer(restaurants, many=True)
        return Response(serializer.data)

    # def post(self, request):
    #     serializer = RestaurantSerializer(data=request.data)
    #     if serializer.is_valid():
    #         restaurant = Restaurant(**serializer.validated_data)
    #         restaurant.save(using='external')
    #         return Response(RestaurantSerializer(restaurant).data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RestaurantDetail(APIView):
    permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        try:
            return Restaurant.objects.using('external').get(pk=pk)
        except Restaurant.DoesNotExist:
            return None

    def get(self, request, pk):
        restaurant = self.get_object(pk)
        if not restaurant:
            return Response({"error": "لم يتم العثور على المطعم"}, status=status.HTTP_404_NOT_FOUND)
        serializer = RestaurantSerializer(restaurant)
        return Response(serializer.data)

    # def put(self, request, pk):
    #     restaurant = self.get_object(pk)
    #     if not restaurant:
    #         return Response({"error": "لم يتم العثور على المطعم"}, status=status.HTTP_404_NOT_FOUND)

    #     serializer = RestaurantSerializer(restaurant, data=request.data)
    #     if serializer.is_valid():
    #         for attr, value in serializer.validated_data.items():
    #             setattr(restaurant, attr, value)
    #         restaurant.save(using='external')
    #         return Response(RestaurantSerializer(restaurant).data)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # def delete(self, request, pk):
    #     restaurant = self.get_object(pk)
    #     if not restaurant:
    #         return Response({"error": "لم يتم العثور على المطعم"}, status=status.HTTP_404_NOT_FOUND)
    #     restaurant.delete(using='external')
    #     return Response(status=status.HTTP_204_NO_CONTENT)
