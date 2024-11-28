from django.db import models

class Order(models.Model):
    number = models.IntegerField()
    date = models.DateField()
    telephone_number = models.CharField(max_length=20)
    payment_status = models.CharField(max_length=20)
    order_status = models.CharField(max_length=20)

