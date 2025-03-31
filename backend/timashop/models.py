# backend/timashop/models.py
from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name="نام کالا")
    price = models.PositiveIntegerField(verbose_name="قیمت (تومان)")
    stock = models.PositiveIntegerField(verbose_name="موجودی")

    def __str__(self):
        return self.name

class Sale(models.Model):
    product = models.ForeignKey(Product, on_delete=models.PROTECT, verbose_name="کالا")
    quantity = models.PositiveIntegerField(verbose_name="تعداد")
    sale_date = models.DateTimeField(auto_now_add=True, verbose_name="تاریخ فروش")

    def total_price(self):
        return self.product.price * self.quantity
