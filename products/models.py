from django.db import models
from category.models import Category


# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.IntegerField()
    quantity = models.IntegerField(default=0)
    description = models.TextField(null=True, blank=True)

    def __str__(self) -> str:
        return f"{self.name}, {self.category}"
