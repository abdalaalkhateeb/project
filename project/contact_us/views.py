# views.py
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.core.mail import send_mail
from .serializers import ContactUsSerializer

@api_view(['POST'])
def contact_us(request):
    serializer = ContactUsSerializer(data=request.data)
    if serializer.is_valid():
        name = serializer.validated_data['name']
        email = serializer.validated_data['email']
        message = serializer.validated_data['message']

        send_mail(
            subject=f"رسالة جديدة من {name}",
            message=f"الرسالة:\n{message}\n\nمن: {email}",
            from_email='your_email@example.com',
            recipient_list=['your_email@example.com'],
            fail_silently=False,
        )

        return Response({'message': 'تم إرسال الرسالة بنجاح!'}, status=status.HTTP_200_OK)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
