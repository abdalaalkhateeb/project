# chat/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import requests
from django.conf import settings

class GeminiAPIView(APIView):
    def post(self, request):
        user_input = request.data.get("message", "")

        GEMINI_API_KEY = "YOUR_GEMINI_API_KEY"  # أو settings.GEMINI_API_KEY لو تستخدم dotenv
        url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent?key={GEMINI_API_KEY}"

        payload = {
            "contents": [
                {"role": "user", "parts": [{"text": user_input}]}
            ]
        }

        try:
            response = requests.post(url, json=payload)
            response_data = response.json()

            reply = response_data["candidates"][0]["content"]["parts"][0]["text"]

            return Response({"response": reply}, status=status.HTTP_200_OK)

        except Exception as e:
            return Response(
                {"error": "حدث خطأ أثناء الاتصال بـ Gemini.", "details": str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
