from django.urls import path
from .views import stock_price

urlpatterns = [
    path('api/stocks/<str:symbol>/', stock_price, name='stock_price'),
]
