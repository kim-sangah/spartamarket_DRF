from django.urls import path
from . import views


app_name = "accounts"
urlpatterns = [
    path('', views.AccountCreate.as_view(), name='signup'),
    path('login/', views.Login.as_view(), name='login'),
    path('<str:username>/', views.Profile.as_view() , name='profile'),
    # username이 login인 경우가 생긴다면 다 프로필로 가기에 'profile/<str:username>/'으로 수정이 필요!
]