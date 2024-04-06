from django.db import models

class Category(models.Model):
    # Define choices for different boards
    ICSE = 'ICSE'
    CBSE = 'CBSE'
    STATE_BOARD = 'State Board'

    BOARD_CHOICES = [
        (ICSE, 'ICSE'),
        (CBSE, 'CBSE'),
        (STATE_BOARD, 'State Board'),
    ]

    name = models.CharField(max_length=100, choices=BOARD_CHOICES)

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
