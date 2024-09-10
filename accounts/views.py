from django.shortcuts import get_object_or_404
from .models import Account
from .serializers import AccountSerializer, ProfileSerializer
from rest_framework import status
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.views import TokenObtainPairView


class AccountCreate(generics.CreateAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer

#class CreateAPIView(mixins.CreateModelMixin,GenericAPIView):
#    def post(self, request, *args, **kwargs):
#        return self.create(request, *args, **kwargs)
# generics 내 CreateAPIView가 객체를 알아서 저장


class Login(TokenObtainPairView):
    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
        except:
            return Response(
                {"로그인 실패 : 아이디와 비밀번호를 확인해주세요."},
                status=status.HTTP_401_UNAUTHORIZED
            )
        return Response(serializer.validated_data, status=status.HTTP_200_OK)


class Profile(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, username):
        account = get_object_or_404(Account, username=username)
        serializer = ProfileSerializer(account)
        return Response(serializer.data)