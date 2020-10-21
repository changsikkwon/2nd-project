from django.db      import models

class OrderItem(models.Model):
    order       = models.ForeignKey('Order', on_delete = models.CASCADE)
    product     = models.ForeignKey('product.Product', on_delete = models.CASCADE)
    quantity    = models.PositiveIntegerField(default = 1)

class Order(models.Model):
    total_price = models.DecimalField(max_digits = 10, decimal_places = 2, null = True)
    user        = models.ForeignKey('user.User', on_delete = models.CASCADE)
    order_item  = models.ManyToManyField('product.Product', through = OrderItem)

    class Meta:
        db_table = "orders"