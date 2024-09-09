from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from . import views


app_name = "accounts"
urlpatterns = [
    path('', views.AccountCreate.as_view(), name='signup'),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # refresh 토큰도 같이 만듬
    path('<str:username>/', views.Profile.as_view() , name='profile'),
    # username이 login인 경우가 생긴다면 다 프로필로 가기에 'profile/<str:username>/'으로 수정이 필요!
]