from django.urls import path
from .views import *

urlpatterns = [
    path('item/<int:id>/', item_detail, name='item'),
    path('order/<int:id>/', order_detail, name='order'),
    path('buy/<int:id>/', get_item_stripe_session_id, name='buy_item'),
    path('buy_order/<int:id>/', get_order_stripe_session_id, name='buy_order'),
    path('item_payment_intent/<int:id>/', get_item_stripe_payment_intent, name='item_payment_intent'),
    path('order_payment_intent/<int:id>/', get_order_stripe_payment_intent, name='order_payment_intent'),
]
