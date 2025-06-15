from rest_framework import serializers
from core.models import Room, Booking, Payment, Restaurant, Tour
from accounts.models import User

class BookingSerializer(serializers.ModelSerializer):
    booking_type = serializers.ChoiceField(
        choices=[('room', 'Room'), ('restaurant', 'Restaurant'), ('tour', 'Tour')],
        required=True
    )

    class Meta:
        model = Booking
        fields = ['booking_id', 'user', 'entity_id', 'booking_type', 'booking_date', 'status', 'total_cost']
        read_only_fields = ['user', 'booking_id']

    def validate(self, data):
        booking_type = data.get('booking_type')
        entity_id = data.get('entity_id')

        # استخدام قاعدة البيانات الخارجية للتحقق
        if booking_type and entity_id:
            if booking_type == 'room' and not Room.objects.using('external').filter(room_id=entity_id).exists():
                raise serializers.ValidationError("Room does not exist.")
            elif booking_type == 'restaurant' and not Restaurant.objects.using('external').filter(restaurant_id=entity_id).exists():
                raise serializers.ValidationError("Restaurant does not exist.")
            elif booking_type == 'tour' and not Tour.objects.using('external').filter(tour_id=entity_id).exists():
                raise serializers.ValidationError("Tour does not exist.")
        return data

    def create(self, validated_data):
        email = self.context['request'].user.username
        try:
            db_user = User.objects.using('external').get(email=email)
        except User.DoesNotExist:
            raise serializers.ValidationError("User not found in external database.")

        booking = Booking(**validated_data)
        booking.user = db_user
        booking.save(using='external')
        return booking
    
class PaymentSerializer(serializers.Serializer):
    booking_id = serializers.IntegerField()
    amount = serializers.DecimalField(max_digits=10, decimal_places=2)
    payment_method = serializers.CharField(max_length=50)

    def validate(self, data):
        request = self.context['request']
        email = request.user.username

        try:
            booking = Booking.objects.using('external').get(booking_id=data['booking_id'], user__email=email)
        except Booking.DoesNotExist:
            raise serializers.ValidationError("Booking not found or does not belong to user.")

        if booking.status != 'pending':
            raise serializers.ValidationError("Booking must be pending.")

        if data['amount'] != booking.total_cost:
            raise serializers.ValidationError("Amount does not match booking total.")

        self.context['booking'] = booking
        return data
