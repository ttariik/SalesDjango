from django.db import models

# Create your models here.

class Customer(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    newsletter_abo = models.BooleanField(default=True)
    email_address = models.CharField(max_length=30, blank=True, default="")
    account = models.FloatField(blank=True, null=True)

    def __str__():
        return ""

class Product(models.Model):
    name = models.CharField(max_length=30)
    price = models.FloatField()

class Bill(models.Model):
    total_amount = models.FloatField()
    is_paid = models.BooleanField(default=False)

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product, through="ProductType")
    bill = models.OneToOneField(Bill, on_delete=models.CASCADE)

class ProductType(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    type_name = models.CharField(max_length=300)

