# Generated by Django 5.0 on 2023-12-27 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0008_alter_order_discount_alter_order_tax'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='currency',
            field=models.CharField(choices=[('rub', 'Рубль'), ('usd', 'Доллар')], default='rub', max_length=3, verbose_name='Валюта'),
        ),
        migrations.AddField(
            model_name='order',
            name='currency',
            field=models.CharField(blank=True, choices=[('rub', 'Рубль'), ('usd', 'Доллар')], editable=False, max_length=3, null=True, verbose_name='Валюта'),
        ),
        migrations.AlterField(
            model_name='discount',
            name='value',
            field=models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Размер скидки'),
        ),
        migrations.AlterField(
            model_name='order',
            name='total',
            field=models.DecimalField(blank=True, decimal_places=2, editable=False, max_digits=10, null=True, verbose_name='Итоговая цена'),
        ),
        migrations.AlterField(
            model_name='tax',
            name='value',
            field=models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Ставка'),
        ),
    ]
