from django.db import models

# Create your models here.
class emp(models.Model):
    eno=models.IntegerField()
    ename=models.CharField(max_length=20)
    esal=models.FloatField()
    eaddr=models.CharField(max_length=20)
