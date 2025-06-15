from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User as AuthUser
from rest_framework_simplejwt.tokens import RefreshToken
from datetime import date
from core.models import Attraction

class TestAttractionAPI(APITestCase):
    databases = {'default'}  # ✅ استخدام قاعدة داخلية فقط

    def setUp(self):
        # إنشاء مستخدم داخلي لاختبار JWT
        self.auth_user = AuthUser.objects.create_user(username="user@example.com", password="123456")
        refresh = RefreshToken.for_user(self.auth_user)
        self.access_token = str(refresh.access_token)

        # إدخال بيانات وهمية في قاعدة default
        Attraction.objects.create(
            name="Giza Pyramids",
            location="Giza",
            type="Historical",
            description="Ancient pyramids of Egypt",
            hours_of_operation="8 AM - 5 PM"
        )

    def test_list_attractions(self):
        # إرسال الطلب مع التوكن
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.access_token}')
        response = self.client.get("/attractions/")

        self.assertEqual(response.status_code, 200)
        self.assertTrue(len(response.data) >= 1)
        self.assertEqual(response.data[0]["name"], "Giza Pyramids")
