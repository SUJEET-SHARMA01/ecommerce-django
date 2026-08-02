from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Product(models.Model):
    category = models.ForeignKey(
    Category,
    on_delete=models.CASCADE,
    related_name="products"
)
    name = models.CharField(max_length = 200)
    description = models.TextField()
    price = models.DecimalField(max_digits = 10,decimal_places = 2)
    stock = models.PositiveIntegerField()
    image = models.ImageField(upload_to="products/")

    def __str__(self):
        return self.name

class Cart(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.product.name} ({self.quantity})"

