from django.db import models

# cart/models.py
from django.db import models
from django.contrib.auth.models import User
from products.models import Product

class CartItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    class Meta:
        unique_together = ['user', 'product']  # Ensure a user can't add the same product twice

    def __str__(self):
        return f'{self.product.name} - {self.quantity}'
