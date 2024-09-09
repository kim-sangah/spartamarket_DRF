from django.shortcuts import get_object_or_404
from .models import Account
from .serializers import AccountSerializer, ProfileSerializer
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated


class AccountCreate(generics.CreateAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer

#class CreateAPIView(mixins.CreateModelMixin,
#                    GenericAPIView):
#    """
#    Concrete view for creating a model instance.
#    """
#    def post(self, request, *args, **kwargs):
#        return self.create(request, *args, **kwargs)


class Profile(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, username):
        account = self.get_object_or_404(Account, pk=username)
        serializer = ProfileSerializer(account)
        return Response(serializer.data)