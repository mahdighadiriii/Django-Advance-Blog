from django.urls import path, include
from .. import views
from rest_framework.authtoken.views import ObtainAuthToken
from ..views import CustomDicardAuthtoken
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)




urlpatterns = [
    # registration
    path('registration/', views.RegistrationApiView.as_view(), name='registration'),
    #email 
    path('test-email', views.TestEmailSend.as_view(), name='test-email'),
    # activation
    path('activation/confirm/<str:token>', views.ActivationApiView.as_view(), name='activation'),
    # change password
    path('change-password/',views.ChangePasswordApiView.as_view(), name='change-password'),
    # token login
    path('token/login/', views.CustomObtainAuthToken.as_view(), name='token-login'),
    path('token/logout/', views.CustomDicardAuthtoken.as_view(), name='token-logout'),
    
    # jwt login
    path('jwt/create/',views.CustomTokenObtainPairView.as_view(), name='jwt-create'),
    path('jwt/refresh/',TokenRefreshView.as_view(), name='jwt-refresh'),
    path('jwt/verify/',TokenVerifyView.as_view(), name='jwt-verify'),
]