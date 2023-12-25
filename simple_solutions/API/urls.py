from django.urls import path
from .views import *

urlpatterns = [
    path('item/<int:id>/', item_detail, name='item'),
    path('order/<int:id>/', order_detail, name='order'),
    path('buy/<int:id>/', buy_item, name='buy_item'),
    path('buy_order/<int:id>/', buy_order, name='buy_order'),
]
