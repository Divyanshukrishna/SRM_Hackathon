from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)

class Category1(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    field1 = models.CharField(max_length=100)
    field2 = models.IntegerField()

class Category2(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    field1 = models.CharField(max_length=100)
    field2 = models.DecimalField(max_digits=10, decimal_places=2)

class Category3(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    field1 = models.CharField(max_length=100)
    field2 = models.BooleanField()

