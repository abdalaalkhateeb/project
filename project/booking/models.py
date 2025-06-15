from django.db import models

class FakeBooking(models.Model):
    booking_type = models.CharField(max_length=50)
    entity_id = models.IntegerField()
    booking_date = models.DateField()
    status = models.CharField(max_length=50)
    total_cost = models.DecimalField(max_digits=10, decimal_places=2)

    def is_pending(self):
        return self.status == 'pending'

    class Meta:
        app_label = 'booking'