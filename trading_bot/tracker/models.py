from django.db import models

# Create your models here.
class BTCUSDT(models.Model):
    open = models.IntegerField()
    close = models.IntegerField()
    
