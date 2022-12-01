from django.db import models

# Create your models here.
class Chart(models.Model):
    date = models.CharField(max_length=200)
    trade_code = models.CharField(max_length=200)
    high =models.CharField(max_length=200)
    low = models.CharField(max_length=200)
    open = models.CharField(max_length=200)
    close = models.CharField(max_length=200)
    volume = models.CharField(max_length=200)

    
