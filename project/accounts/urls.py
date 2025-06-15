from django.urls import path
from .views import SignUpView, SignIn, SignOut,get_users, ForgotPasswordView , ResetPasswordView

urlpatterns = [
    path("signin/", SignIn.as_view(), name="api_sign_in"),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('forgetpassword/', ForgotPasswordView.as_view(), name='forget_password'),
    path('signout/', SignOut.as_view(), name='sign_out'),
    path('reset-password/', ResetPasswordView.as_view(), name='reset-password'),
    path('getusers/', get_users.as_view(), name='get_users'),
] 
