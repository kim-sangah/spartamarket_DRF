from django.shortcuts import get_object_or_404
# from django.core.paginator import Paginator
from .models import Product
from .serializers import ProductSerializer
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response


class ProductAPIView(APIView):
    # 물건 글 목록
    def get(self, request):
        products = Product.objects.all()
        # paginator = Paginator(products, 10)  
        # page_number = request.GET.get("page")
        # page_obj = paginator.get_page(page_number)
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

    # 물건 글 작성 (물건 인스턴스 생성)
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