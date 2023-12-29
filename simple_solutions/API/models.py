from django.db import models
from decimal import Decimal
from .resources import CURRENCY_CHOICES, RUSSIAN_RUBLE


class Item(models.Model):
    """Товар"""
    name = models.CharField('Название', max_length=100)
    description = models.TextField('Описание')
    price = models.DecimalField('Цена', max_digits=10, decimal_places=2)
    currency = models.CharField('Валюта', max_length=3, choices=CURRENCY_CHOICES, default=RUSSIAN_RUBLE)

    def __str__(self):
        return f"id:{self.id} {self.name}"

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'


class Discount(models.Model):
    """Скидка"""
    name = models.CharField('Название', max_length=100)
    value = models.DecimalField('Размер скидки', max_digits=5, decimal_places=2)

    def __str__(self):
        return f"id:{self.id} {self.name}"

    class Meta:
        verbose_name = 'Скидка'
        verbose_name_plural = 'Скидки'


class Tax(models.Model):
    """Налог"""
    name = models.CharField('Название', max_length=100)
    value = models.DecimalField('Ставка', max_digits=5, decimal_places=2)

    def __str__(self):
        return f"id:{self.id} {self.name}"

    class Meta:
        verbose_name = 'Налог'
        verbose_name_plural = 'Налоги'


class Order(models.Model):
    """Заказ"""
    items = models.ManyToManyField(Item, verbose_name='Товар')
    discount = models.ManyToManyField(Discount, verbose_name='Скидка', blank=True)
    tax = models.ManyToManyField(Tax, verbose_name='Налог', blank=True)
    total = models.DecimalField(
        'Итоговая цена',
        max_digits=10,
        decimal_places=2,
        blank=True,
        null=True,
        editable=False
    )
    currency = models.CharField(
        'Валюта',
        max_length=3,
        choices=CURRENCY_CHOICES,
        blank=True,
        null=True,
        editable=False
    )

    def __str__(self):
        return f"id:{self.id}  Final Order Value:{self.total} {self.currency}"

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    # Вычисление конечной стоимости заказа, с учётом скидок и налогов
    def calculate_total(self):
        total = self.items.aggregate(total=models.Sum('price'))['total'] or Decimal('0')
        discounts_total = self.discount.aggregate(total=models.Sum('value'))['total'] or Decimal('0')
        taxes_total = self.tax.aggregate(total=models.Sum('value'))['total'] or Decimal('0')
        if discounts_total == Decimal('0'):
            discount_price = total
        else:
            discount_price = total - (total * (discounts_total / Decimal('100')))
        if taxes_total == Decimal('0'):
            return discount_price
        else:
            return discount_price + (discount_price * (taxes_total / Decimal('100')))

    def save(self, *args, **kwargs):
        super(Order, self).save(*args, **kwargs)

        if not self.currency and self.items.exists():
            self.currency = self.items.first().currency
            super(Order, self).save(*args, **kwargs)

        if self.items.exists():
            self.total = self.calculate_total()
            super(Order, self).save(update_fields=['total'])
        else:
            self.total = None
