from django.db import models

# Create your models here.
class payment(models.Models):
     amount = models.FloatField(max_length=30)
     received_by = models.IntegerField(max_length=10)
     paid_by = models.IntegerField(max_length=10)
     created_at = models.DateField()
     updated_at = models.DateField()
     id = models.AutoField(primary_key=True)