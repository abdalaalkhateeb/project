# booking/tests/test_models.py
from django.test import TestCase
from .models import FakeBooking
from datetime import date

class TestBookingLogic(TestCase):
    def test_is_pending(self):
        booking = FakeBooking(
            booking_type="room",
            entity_id=1,
            booking_date=date.today(),
            status="pending",
            total_cost=200
        )
        self.assertTrue(booking.is_pending())

    def test_is_not_pending(self):
        booking = FakeBooking(
            booking_type="room",
            entity_id=1,
            booking_date=date.today(),
            status="completed",
            total_cost=200
        )
        self.assertFalse(booking.is_pending())
