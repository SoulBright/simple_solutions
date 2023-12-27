from django.db import models
from django.db.models.signals import m2m_changed, post_save
from django.dispatch import receiver
from decimal import Decimal
from .models import Order


@receiver(m2m_changed, sender=Order.items.through)
@receiver(m2m_changed, sender=Order.discount.through)
@receiver(m2m_changed, sender=Order.tax.through)
def update_total(sender, instance, action, **kwargs):
    """Сигнал, который обновляет поле `total` при изменении связей ManyToMany."""
    if action in ['post_add', 'post_remove', 'post_clear']:
        items_price = instance.items.aggregate(total=models.Sum('price'))['total'] or 0
        discount_value = instance.discount.aggregate(total=models.Sum('value'))['total'] or 0
        tax_value = instance.tax.aggregate(total=models.Sum('value'))['total'] or 0
        discount_price = items_price - (items_price * (discount_value / Decimal('100')))
        instance.total = discount_price + (discount_price * (tax_value / Decimal('100')))
        instance.save()
