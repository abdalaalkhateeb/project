# from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth import authenticate
from rest_framework.exceptions import AuthenticationFailed
from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from core.models import User  # إذا كان الموديل موجود في core

class SignUpSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['user_id', 'email', 'name', 'password']

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password'])  # تشفير الباسورد
        return super().create(validated_data)

# class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
#     username_field = 'email'  # نستخدم البريد بدلاً من username

#     def validate(self, attrs):
#         email = attrs.get("email")
#         password = attrs.get("password")

#         user = authenticate(username=email, password=password)

#         if not user:
#             raise AuthenticationFailed("البريد الإلكتروني أو كلمة المرور غير صحيحة")

#         data = super().validate(attrs)
#         return data
