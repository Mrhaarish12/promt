from django.db import models

class Promotionfmodel(models.Model):
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)
    gender = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    rname = models.CharField(max_length=100)
    account_no = models.CharField(max_length=200)
    bank_name = models.CharField(max_length=100)
    acctype = models.CharField(max_length=100)
    ifsc = models.CharField(max_length=100)
    biz_name = models.CharField(max_length=100)
    biz_type = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    weburl = models.CharField(max_length=200)
    class Meta:
        db_table="promotionform1"
    