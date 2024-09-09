from rest_framework import serializers
from .models import Account

# 계정 회원가입
class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['username', 'password', 'email', 'name', 'nickname', 'birthday', 'gender', 'introduction',]


# 계정 로그인
class loginSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['username', 'password', 'email', 'name', 'nickname', 'birthday', 'gender', 'introduction',]


# 계정 프로필
class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['username', 'email', 'name', 'nickname', 'birthday', 'gender', 'introduction',]