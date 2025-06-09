# core/views.py

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Attraction, Hotel, Restaurant, Review, Tour
from .serializers import AttractionSerializer, HotelSerializer, RestaurantSerializer, ReviewSerializer, TourSerializer

@api_view(['GET'])
def hotel_list(request):
    hotels = Hotel.objects.all()
    serializer = HotelSerializer(hotels, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def restaurant_list(request):
    restaurants = Restaurant.objects.all()
    serializer = RestaurantSerializer(restaurants, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def tour_list(request):
    tours = Tour.objects.all()
    serializer = TourSerializer(tours, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def attraction_list(request):
    attractions = Attraction.objects.all()
    serializer = AttractionSerializer(attractions, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def review_list(request):
    reviews = Review.objects.all()
    serializer = ReviewSerializer(reviews, many=True)
    return Response(serializer.data)

