from django.shortcuts import render
from django.http import JsonResponse
from dotenv import load_dotenv
from stripe import stripe
from .models import *
import os

load_dotenv()
stripe.api_key = os.getenv('SRTIPE_SECRET_KEY')


def item_detail(request, id):
    try:
        item = Item.objects.get(pk=id)
    except Item.DoesNotExist:
        return JsonResponse({'error': 'Item not found'}, status=404)

    context = {
        'item': item,
        'stripe_public_key': os.getenv('SRTIPE_PUBLISHABLE_KEY'),
    }
    return render(request, 'item.html', context)


def order_detail(request, id):
    try:
        order = Order.objects.get(pk=id)
    except Order.DoesNotExist:
        return JsonResponse({'error': 'Order not found'}, status=404)

    context = {
        'order': order,
        'item_names': list(order.discount.values_list('name', flat=True)),
        'discount_names': list(order.discount.values_list('name', flat=True)),
        'tax_names': list(order.tax.values_list('name', flat=True)),
        'stripe_public_key': os.getenv('SRTIPE_PUBLISHABLE_KEY'),
    }
    return render(request, 'order.html', context)


def get_item_stripe_session_id(request, id):
    try:
        item = Item.objects.get(id=id)
    except Item.DoesNotExist:
        return JsonResponse({'error': 'Item not found'}, status=404)

    # Создание Stripe сессии
    session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=[{
            'price_data': {
                'currency': item.currency,
                'product_data': {
                    'name': item.name,
                    'description': item.description,
                },
                'unit_amount': int(item.price * 100),
            },
            'quantity': 1,
        }],
        mode='payment',
        success_url='https://example.com/success/',
        cancel_url='https://example.com/cancel/',
    )

    return JsonResponse({'session_id': session.id})


def get_order_stripe_session_id(request, id):
    try:
        order = Order.objects.get(id=id)
    except Order.DoesNotExist:
        return JsonResponse({'error': 'order not found'}, status=404)

    session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=[{
            'price_data': {
                'currency': order.currency,
                'product_data': {
                    'name': ', '.join(order.items.values_list('name', flat=True)),
                },
                'unit_amount': int(order.total * 100),
            },
            'quantity': 1,
        }],
        mode='payment',
        success_url='https://example.com/success/',
        cancel_url='https://example.com/cancel/',
    )

    return JsonResponse({'session_id': session.id})


def get_item_stripe_payment_intent(request, id):
    try:
        item = Item.objects.get(id=id)
    except Item.DoesNotExist:
        return JsonResponse({'error': 'Item not found'}, status=404)

    # Создание Stripe Payment Intent
    intent = stripe.PaymentIntent.create(
        amount=int(item.price * 100),  # Сумма в копейках или центах
        currency=item.currency,  # Валюта
        description=item.name  # Описание платежа
    )

    return JsonResponse({'client_secret': intent.client_secret})


def get_order_stripe_payment_intent(request, id):
    try:
        order = Order.objects.get(id=id)
    except Order.DoesNotExist:
        return JsonResponse({'error': 'Item not found'}, status=404)

    intent = stripe.PaymentIntent.create(
        amount=int(order.total * 100),
        currency=order.currency,
    )

    return JsonResponse({'client_secret': intent.client_secret})
