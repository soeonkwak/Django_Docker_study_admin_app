from django.contrib import admin
from django.urls import path

from .views import ProductViewSet, UserAPIView

urlpatterns = [
    path('products', ProductViewSet.as_view({
        'get': 'list', #http://localhost:8000/api/products
        'post': 'create' #http://localhost:8000/api/products
    })),
    path('products/<str:pk>', ProductViewSet.as_view({
        'get': 'retrieve',  #http://localhost:8000/api/products/1
        'put': 'update',
        'delete': 'destroy'
    })),
    path('user', UserAPIView.as_view())
]
