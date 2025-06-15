from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from core.models import Booking, Payment
from .serializers import  BookingSerializer, PaymentSerializer
from rest_framework.permissions import IsAuthenticated
# from rest_framework.exceptions import PermissionDenied
from accounts.models import User 



class BookingPersonalView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, format=None):
        serializer = BookingSerializer(data=request.data, context={'request': request})
        
        if serializer.is_valid():
            try:
                # جلب المستخدم من قاعدة البيانات الخارجية
                db_user = User.objects.using('external').get(email=request.user.username)
            except User.DoesNotExist:
                return Response({"error": "User not found in external DB"}, status=status.HTTP_404_NOT_FOUND)

            # استخدام validated_data لإنشاء الحجز يدويًا
            validated_data = serializer.validated_data
            booking = Booking(**validated_data)
            booking.user = db_user
            booking.save(using='external')

            # إرجاع البيانات (اختياري: قد تحتاج تحديث serializer بالـ booking الجديد)
            return Response({"message": "Booking created"}, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class BookingInfoView(APIView):
    permission_classes = [IsAuthenticated]

    def get_user(self, request):
        return User.objects.using('external').get(email=request.user.username)

    def get(self, request, booking_id, format=None):
        try:
            db_user = self.get_user(request)
            booking = Booking.objects.using('external').get(booking_id=booking_id, user_id=db_user.user_id)
            serializer = BookingSerializer(booking)
            return Response(serializer.data)
        except User.DoesNotExist:
            return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)
        except Booking.DoesNotExist:
            return Response({"error": "Booking not found"}, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, booking_id, format=None):
        try:
            db_user = self.get_user(request)
            booking = Booking.objects.using('external').get(booking_id=booking_id, user_id=db_user.user_id)
            serializer = BookingSerializer(booking, data=request.data, context={'request': request})
            if serializer.is_valid():
                updated_booking = serializer.validated_data
                for attr, value in updated_booking.items():
                    setattr(booking, attr, value)
                booking.save(using='external')
                return Response(BookingSerializer(booking).data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except User.DoesNotExist:
            return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)
        except Booking.DoesNotExist:
            return Response({"error": "Booking not found"}, status=status.HTTP_404_NOT_FOUND)


class BookingSummaryView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, booking_id, format=None):
        try:
            db_user = User.objects.using('external').get(email=request.user.username)
            booking = Booking.objects.using('external').get(booking_id=booking_id, user_id=db_user.user_id)
            serializer = BookingSerializer(booking)
            return Response(serializer.data)
        except User.DoesNotExist:
            return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)
        except Booking.DoesNotExist:
            return Response({"error": "Booking not found"}, status=status.HTTP_404_NOT_FOUND)
        
class PaymentView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, format=None):
        serializer = PaymentSerializer(data=request.data, context={'request': request})

        if serializer.is_valid():
            try:
                db_user = User.objects.using('external').get(email=request.user.username)
            except User.DoesNotExist:
                return Response({"error": "User not found in external database."}, status=status.HTTP_404_NOT_FOUND)

            booking = serializer.context['booking']

            payment = Payment(
                user=db_user,
                booking=booking,
                amount=serializer.validated_data['amount'],
                payment_method=serializer.validated_data.get('payment_method'),
                status='completed'
            )
            payment.save(using='external')

            return Response({"message": "Payment processed successfully"}, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
