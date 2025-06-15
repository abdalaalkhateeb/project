import django_filters
from core.models import Hotel, Room

class HotelFilter(django_filters.FilterSet):
       name = django_filters.CharFilter(lookup_expr='icontains')
       location = django_filters.CharFilter(lookup_expr='icontains')
       rating__gte = django_filters.NumberFilter(field_name='rating', lookup_expr='gte')
       available_rooms__gte = django_filters.NumberFilter(field_name='available_rooms', lookup_expr='gte')

       class Meta:
           model = Hotel
           fields = ['name', 'location', 'rating', 'available_rooms']

class RoomFilter(django_filters.FilterSet):
       room_type = django_filters.CharFilter(lookup_expr='icontains')
       price_per_night__lte = django_filters.NumberFilter(field_name='price_per_night', lookup_expr='lte')
       availability = django_filters.BooleanFilter(field_name='availability')
       capacity__gte = django_filters.NumberFilter(field_name='capacity', lookup_expr='gte')
       hotel = django_filters.NumberFilter(field_name='hotel__hotel_id')

       class Meta:
           model = Room
           fields = ['room_type', 'price_per_night', 'availability', 'capacity', 'hotel']