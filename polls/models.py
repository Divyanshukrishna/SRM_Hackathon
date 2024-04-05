from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)

class StateData(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    state = models.CharField(max_length=100)

class StateData1(StateData):
    field1 = models.CharField(max_length=100)
    field2 = models.IntegerField()

class StateData2(StateData):
    field1 = models.CharField(max_length=100)
    field2 = models.DecimalField(max_digits=10, decimal_places=2)

class StateData3(StateData):
    field1 = models.CharField(max_length=100)
    field2 = models.BooleanField()
