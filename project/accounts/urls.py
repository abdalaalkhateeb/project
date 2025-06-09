from django.urls import path
from .views import SignUpView, SignIn, SignOut, ForgetPassword , SignWithGoogle, SignWithApple, get_users

urlpatterns = [
    path("signin/", SignIn.as_view(), name="api_sign_in"),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('forgetpassword/', ForgetPassword.as_view(), name='forget_password'),
    path('signout/', SignOut.as_view(), name='sign_out'),
    path('signwithgoogle/', SignWithGoogle.as_view(), name='sign_with_google'),
    path('signwithApple/', SignWithApple.as_view(), name='sign_with_facebook'),
    path('getusers/', get_users.as_view(), name='get_users'),
]
