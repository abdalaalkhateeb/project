# from django.db import models
# from core.models import User , Payment , Notification
# # Create your models here.
from core.models import User as CoreUser
from django.db import models

User = CoreUser


class OTPCode(models.Model):
    email = models.EmailField()
    otp = models.CharField(max_length=6)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.email} - {self.otp}"
