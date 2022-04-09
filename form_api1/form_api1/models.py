from django.db import models

class Promotionfmodel(models.Model):
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)
    gender = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    class Meta:
        db_table="promotionform1"
    