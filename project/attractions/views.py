from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from core.models import Attraction
from .serializers import AttractionSerializer
from rest_framework.permissions import IsAuthenticated

class AttractionList(APIView):
    permission_classes = [IsAuthenticated]  # ✅ لا يمكن الوصول بدون تسجيل الدخول

    def get(self, request):
        attractions = Attraction.objects.using('external').all()
        serializer = AttractionSerializer(attractions, many=True)
        return Response(serializer.data)

class AttractionDetail(APIView):
    permission_classes = [IsAuthenticated]  # ✅ الحماية بالتوكن

    def get_object(self, pk):
        # محاولة جلب الكائن من قاعدة البيانات الخارجية
        try:
            return Attraction.objects.using('external').get(pk=pk)
        except Attraction.DoesNotExist:
            return None

    def get(self, request, pk):
        # عرض التفاصيل لكائن معين
        attraction = self.get_object(pk)
        if not attraction:
            return Response({"error": "لم يتم العثور على العنصر"}, status=status.HTTP_404_NOT_FOUND)
        serializer = AttractionSerializer(attraction)
        return Response(serializer.data)
