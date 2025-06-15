# account/api_views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.hashers import check_password, make_password
from .serializers import SignUpSerializer 
from rest_framework_simplejwt.tokens import RefreshToken, TokenError  # لو بدك ترجع JWT
from rest_framework_simplejwt.token_blacklist.models import BlacklistedToken, OutstandingToken
from rest_framework.permissions import IsAuthenticated  # لو بدك تحمي بعض الواجهات
from .models import OTPCode,User as ExternalUser
from django.contrib.auth.models import User as AuthUser
import random


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
            return Response({"error": "البريد الإلكتروني وكلمة المرور مطلوبة"}, status=400)
        try:
            # جلب المستخدم من قاعدة البيانات الخارجية
            external_user = ExternalUser.objects.using('external').get(email=email)

            if check_password(password, external_user.password):
                # توليد أو إنشاء مستخدم في قاعدة البيانات الافتراضية فقط لأجل الـ JWT
                auth_user, created = AuthUser.objects.get_or_create(
                    username=external_user.email
                )
                # توليد التوكن باستخدام المستخدم الداخلي
                refresh = RefreshToken.for_user(auth_user)

                return Response({
                    "message": "تم تسجيل الدخول بنجاح",
                    "user_id": external_user.user_id,
                    "name": external_user.name,
                    "email": external_user.email,
                    "access": str(refresh.access_token),
                    "refresh": str(refresh)
                }, status=200)
            else:
                return Response({"error": "كلمة المرور غير صحيحة"}, status=401)
        except ExternalUser.DoesNotExist:
            return Response({"error": "هذا البريد غير مسجل"}, status=404)

class ForgotPasswordView(APIView):
    def post(self, request):
        email = request.data.get("email")

        if not email:
            return Response({"error": "يرجى إدخال البريد الإلكتروني"}, status=400)

        try:
            user = ExternalUser.objects.using('external').get(email=email)
        except ExternalUser.DoesNotExist:
            return Response({"error": "البريد غير موجود"}, status=404)

        otp = str(random.randint(100000, 999999))

        # حذف أي رموز قديمة
        OTPCode.objects.filter(email=email).delete()

        # حفظ OTP في قاعدة البيانات الداخلية
        OTPCode.objects.create(email=email, otp=otp)

        print(f"[DEV] OTP for {email}: {otp}")  # فقط للتجربة

        return Response({"message": "تم إرسال رمز التحقق (للتجربة)"}, status=200)
class ResetPasswordView(APIView):
    def post(self, request):
        email = request.data.get("email")
        otp = request.data.get("otp")
        new_password = request.data.get("new_password")

        if not all([email, otp, new_password]):
            return Response({"error": "البيانات ناقصة: البريد، الرمز، كلمة المرور"}, status=400)

        # التحقق من وجود OTP مطابق للبريد
        if not OTPCode.objects.filter(email=email, otp=otp).exists():
            return Response({"error": "رمز التحقق غير صحيح أو منتهي"}, status=400)

        try:
            # جلب المستخدم من قاعدة external
            user = ExternalUser.objects.using('external').get(email=email)
        except ExternalUser.DoesNotExist:
            return Response({"error": "المستخدم غير موجود"}, status=404)

        # تغيير كلمة المرور بعد التحقق وتشفيرها
        user.password = make_password(new_password)
        user.save(using='external')

        # حذف الرمز بعد الاستخدام
        OTPCode.objects.filter(email=email).delete()

        return Response({"message": "تم تغيير كلمة المرور بنجاح"}, status=200)
    
class get_users(APIView):
    def get(self, request):
        users = ExternalUser.objects.all().values("user_id", "email", "name")
        return Response({"users": list(users)}, status=status.HTTP_200_OK)
    



class SignOut(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            refresh_token = request.data["refresh"]
            token = RefreshToken(refresh_token)
            token.blacklist()  # هذا يُضيف التوكن إلى قائمة Blacklisted
            return Response({"message": "تم تسجيل الخروج بنجاح"}, status=205)

        except KeyError:
            return Response({"error": "التوكن مفقود"}, status=400)

        except TokenError:
            return Response({"error": "التوكن غير صالح أو منتهي"}, status=400)

