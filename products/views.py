from django.shortcuts import get_object_or_404
# from django.core.paginator import Paginator
from .models import Product
from .serializers import ProductSerializer
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes
from rest_framework.pagination import PageNumberPagination


class DefultPagination(PageNumberPagination):
    page_size = 10


class ProductAPIView(APIView):
    # 물건 글 목록
    def get(self, request):
        products = Product.objects.all()
        paginator = DefultPagination()
        paginated_product = paginator.paginate_queryset(products, request)
        serializer = ProductSerializer(paginated_product, many=True)
        return paginator.get_paginated_response(serializer.data)

    # 물건 글 작성 (물건 인스턴스 생성)
    @permission_classes([IsAuthenticated])
    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


class ProductDetailAPIView(APIView):

    def get_object(self, productId):
        return get_object_or_404(Product, pk=productId)

    # 물건 상세 조회
    def get(self, request, productId):
        products = self.get_object(productId)
        serializer = ProductSerializer(products)
        return Response(serializer.data)

    # 물건 상세 수정
    def put(self, request, productId):
        products = self.get_object(productId)
        if products.seller != request.user:
            data = {"message": f"작성자만 수정이 가능합니다"}
            return Response(data, status=status.HTTP_400_BAD_REQUEST)
        serializer = ProductSerializer(products, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

    # 물건 상세 삭제
    def delete(self, request, productId):
        products = self.get_object(productId)
        products.delete()
        data = {"message": f"{productId} 해당 상품이 삭제되었습니다"}
        return Response(data, status=status.HTTP_200_OK)