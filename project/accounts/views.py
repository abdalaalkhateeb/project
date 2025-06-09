# account/api_views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.hashers import check_password
from core.models import User
from .serializers import SignUpSerializer 
from rest_framework_simplejwt.tokens import RefreshToken  # لو بدك ترجع JWT
from rest_framework_simplejwt.token_blacklist.models import BlacklistedToken, OutstandingToken
from rest_framework.permissions import IsAuthenticated  # لو بدك تحمي بعض الواجهات
from google.oauth2 import id_token
from google.auth.transport import requests as google_requests


class SignUpView(APIView):
    def post(self, request):
        serializer = SignUpSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({
                "message": "تم إنشاء المستخدم بنجاح",
                "user_id": user.user_id,
                "email": user.email,
                "name": user.name
            }, status=status.HTTP_201_CREATED)
            
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SignIn(APIView):
    def post(self, request):
        email = request.data.get("email")
        password = request.data.get("password")

        if not email or not password:
            return Response({"error": "البريد الإلكتروني وكلمة المرور مطلوبة"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            user = User.objects.get(email=email)
            if check_password(password, user.password):
                # توليد توكنات JWT إذا كنت تستخدم simplejwt
                refresh = RefreshToken.for_user(user)
                return Response({
                    "message": "تم تسجيل الدخول بنجاح",
                    "user_id": user.user_id,
                    "name": user.name,
                    "email": user.email,
                    "access": str(refresh.access_token),
                    "refresh": str(refresh)
                }, status=status.HTTP_200_OK)
            else:
                return Response({"error": "كلمة المرور غير صحيحة"}, status=status.HTTP_401_UNAUTHORIZED)

        except User.DoesNotExist:
            return Response({"error": "هذا البريد غير مسجل"}, status=status.HTTP_404_NOT_FOUND)

class get_users(APIView):
    def get(self, request):
        users = User.objects.all().values("user_id", "email", "name")
        return Response({"users": list(users)}, status=status.HTTP_200_OK)
    
class ForgetPassword(APIView):
    def post(self, request):
        email = request.data.get("email")
        if not email:
            return Response({"error": "البريد الإلكتروني مطلوب"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            user = User.objects.get(email=email)

            # هنا يمكنك إضافة منطق إعادة تعيين كلمة المرور، مثل إرسال بريد إلكتروني للمستخدم
            return Response({"message": "تم إرسال تعليمات إعادة تعيين كلمة المرور إلى بريدك الإلكتروني"}, status=status.HTTP_200_OK)
        except User.DoesNotExist:
            return Response({"error": "هذا البريد غير مسجل"}, status=status.HTTP_404_NOT_FOUND)
        
class SignWithGoogle(APIView):
    def post(self, request):
        token = request.data.get("id_token")

        if not token:
            return Response({"error": "يرجى إرسال Google ID Token"}, status=400)

        try:
            # تحقق من التوكن
            idinfo = id_token.verify_oauth2_token(token, google_requests.Request(), "GOOGLE_CLIENT_ID")

            email = idinfo.get("email")
            name = idinfo.get("name")

            user, created = User.objects.get_or_create(email=email, defaults={"name": name})

            return Response({
                "message": "تم تسجيل الدخول" if not created else "تم إنشاء المستخدم",
                "user_id": user.user_id,
                "email": user.email,
                "name": user.name
            }, status=201 if created else 200)

        except ValueError:
            return Response({"error": "رمز Google غير صالح"}, status=400)
            
class SignWithApple(APIView):
    def post(self, request):
        email = request.data.get("email")
        name = request.data.get("name")
        if not email or not name:
            return Response({"error": "البريد الإلكتروني والاسم مطلوبان"}, status=status.HTTP_400_BAD_REQUEST)

        # تحقق مما إذا كان المستخدم موجودًا بالفعل
        user, created = User.objects.get_or_create(email=email, defaults={"name": name})

        if created:
            return Response({
                "message": "تم إنشاء المستخدم بنجاح",
                "user_id": user.user_id,
                "email": user.email,
                "name": user.name
            }, status=status.HTTP_201_CREATED)
        else:
            return Response({
                "message": "المستخدم موجود بالفعل",
                "user_id": user.user_id,
                "email": user.email,
                "name": user.name
            }, status=status.HTTP_200_OK)

class SignOut(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            # الحصول على التوكنات الصادرة لهذا المستخدم
            tokens = OutstandingToken.objects.filter(user=request.user)
            for token in tokens:
                # التأكد من عدم كونه محذوفًا أو ملغيًا بالفعل
                try:
                    RefreshToken(token.token).blacklist()
                except Exception:
                    pass

            return Response({"message": "تم تسجيل الخروج بنجاح"}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": "حدث خطأ أثناء تسجيل الخروج"}, status=status.HTTP_400_BAD_REQUEST)





# class SignOut(APIView):
#     def post(self, request):
#         # هنا يمكنك إضافة منطق تسجيل الخروج إذا كنت تستخدم توكنات JWT
#         # مثلاً، يمكنك حذف التوكن من التخزين المحلي أو إبطال التوكن
#         return Response({"message": "تم تسجيل الخروج بنجاح"}, status=status.HTTP_200_OK)

# from rest_framework.permissions import IsAuthenticated

# class DestinationView(APIView):
#     permission_classes = [IsAuthenticated]

#     def get(self, request):
#         return Response({"message": "You are authorized!"})

