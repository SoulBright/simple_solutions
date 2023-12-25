from django.db import models


class Item(models.Model):
    """Товар"""
    name = models.CharField('Название', max_length=100)
    description = models.TextField('Описание')
    price = models.DecimalField('Цена', max_digits=10, decimal_places=2)

    def __str__(self):
        return f"id:{self.id} {self.name}"

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'


class Discount(models.Model):
    """Скидка"""
    name = models.CharField('Название', max_length=100)
    value = models.DecimalField('Размер скидки', max_digits=10, decimal_places=2)

    def __str__(self):
        return f"id:{self.id} {self.name}"

    class Meta:
        verbose_name = 'Скидка'
        verbose_name_plural = 'Скидки'


class Tax(models.Model):
    """Налог"""
    name = models.CharField('Название', max_length=100)
    value = models.DecimalField('Ставка', max_digits=10, decimal_places=2)

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
    total = models.DecimalField('Итоговая цена', max_digits=10, decimal_places=2, blank=True, null=True)

    def __str__(self):
        return f"id:{self.id} {self.total}"

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def calculate_total(self):
        total = self.items.aggregate(total=models.Sum('price'))['total'] or 0
        discounts_total = self.discount.aggregate(total=models.Sum('value'))['total'] or 0
        taxes_total = self.tax.aggregate(total=models.Sum('value'))['total'] or 0
        return total - (discounts_total + taxes_total)

    def save(self, *args, **kwargs):
        super(Order, self).save(*args, **kwargs)

        if self.items.exists():
            self.total = self.calculate_total()
            super(Order, self).save(update_fields=['total'])
        else:
            self.total = None
