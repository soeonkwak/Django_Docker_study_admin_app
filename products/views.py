import random

from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Product, User
from .serializers import ProductSerializer


# Create your views here.

class ProductViewSet(viewsets.ViewSet):
    def list(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = ProductSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.date, status=status.HTTP_201_CREATED)

    def retrieve(self, request, pk=None):
        product = Product.objects.get(id=pk)
        serializer = ProductSerializer(product)
        return Response(serializer.data)

    def update(self, request, pk=None):
        product = Product.objects.get(id=pk)  # product 객체 쓸거니까 써주고 <- serializer에서 model값이 product라서!?
        serializer = ProductSerializer(instance=product,
                                       data=request.data)  # serializer 구해야 되는데 ProductSerializer랑 같음. arg1 : 우리가 원래 갖고 있는 데이터, arg2: request로 부터 받은 update 될 값
        serializer.is_valid(raise_exception=True)  # 위랑 마찬가지로 serializer 값 검증?
        serializer.save()  # 검증 통과하면 save
        return Response(serializer.date, status=status.HTTP_202_ACCEPTED)

    def destroy(self, request, pk=None):
        product = Product.objects.get(id=pk)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class UserAPIView(APIView): #우리는 .. rest_framework에서 제공하는 APIView 사용할 거 ..
    def get(self, _):
        users = User.objects.all()
        user = random.choice(users)
        return Response({
            "id": user.id
        })
