from django.db import models
from Guest.models import *

# Create your models here.

class tbl_editorbooking(models.Model):
    editor_id=models.ForeignKey(tbl_editorregistration,on_delete=models.CASCADE,null=True)
    photographer_id=models.ForeignKey(tbl_photographerregistration,on_delete=models.CASCADE,null=True)
    booking_date=models.DateField()
    booked_date=models.DateField(auto_now_add=True)
    payment_amount=models.IntegerField(default=0)
    payment_status=models.IntegerField(default=0)
    ebooking_description = models.CharField(max_length=30)
    ebooking_vstatus=models.IntegerField(default=0)

class tbl_modelbooking(models.Model):
    model_id=models.ForeignKey(tbl_modelregistration,on_delete=models.CASCADE,null=True)
    photographer_id=models.ForeignKey(tbl_photographerregistration,on_delete=models.CASCADE,null=True)
    booking_date=models.DateField()
    booked_date=models.DateField(auto_now_add=True)
    payment_amount=models.IntegerField(default=0)
    payment_status=models.IntegerField(default=0)
    mbooking_description = models.CharField(max_length=30)
    mbooking_vstatus=models.IntegerField(default=0)
