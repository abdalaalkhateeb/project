from django.urls import path
from .views import BookingPersonalView, BookingInfoView, BookingSummaryView, PaymentView

urlpatterns = [
    path('', BookingPersonalView.as_view(), name='booking-create'),
    path('<int:booking_id>/', BookingInfoView.as_view(), name='booking-info'),
    path('<int:booking_id>/summary/', BookingSummaryView.as_view(), name='booking-summary'),
    path('payment/', PaymentView.as_view(), name='payment-create'),
]