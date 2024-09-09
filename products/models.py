from django.db import models
from accounts.models import Account


class Product(models.Model):
    seller = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='products')
    title = models.CharField(max_length=50)
    content = models.TextField(max_length=1000)
    image = models.ImageField(upload_to='prodcuts/', blank=True, null=True)