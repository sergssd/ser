from django.db import models
from shop.models import Product


class Order(models.Model):
    first_name = models.CharField(max_length=50, verbose_name='фамилия')
    last_name = models.CharField(max_length=50, verbose_name='имя')
    phone = models.IntegerField(max_length=20, verbose_name='телефон')
    email = models.EmailField()
    address = models.CharField(max_length=250, verbose_name='адрес')
    postal_code = models.CharField(max_length=20, verbose_name='индекс')
    city = models.CharField(max_length=100, verbose_name='город')
    created = models.DateTimeField(auto_now_add=True, verbose_name='создан')
    updated = models.DateTimeField(auto_now=True, verbose_name='обновлен')
    paid = models.BooleanField(default=False, verbose_name='оплачено')

    class Meta:
        ordering = ('-created',)
        verbose_name = 'заказ'
        verbose_name_plural = 'закази'

    def __str__(self):
        return 'Order {}'.format(self.id)

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='order_items', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='цена')
    quantity = models.PositiveIntegerField(default=1, verbose_name='количество')

    class Meta:
        verbose_name = 'заказ. товар'
        verbose_name_plural = 'заказа. товари'
    def __str__(self):
        return '{}'.format(self.id)

    def get_cost(self):
        return self.price * self.quantity
