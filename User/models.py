from django.db import models
from Guest.models import *

# Create your models here.

class tbl_photographerbooking(models.Model):
    user_id=models.ForeignKey(tbl_userregistration,on_delete=models.CASCADE,null=True)
    photographer_id=models.ForeignKey(tbl_photographerregistration,on_delete=models.CASCADE,null=True)
    booking_date=models.DateField()
    booked_date=models.DateField(auto_now_add=True)
    payment_amount=models.IntegerField(default=0)
    payment_status=models.IntegerField(default=0)
    pbooking_description = models.CharField(max_length=30)
    pbooking_vstatus=models.IntegerField(default=0)

class tbl_like(models.Model):
    post = models.ForeignKey(tbl_post,on_delete=models.CASCADE)
    user = models.ForeignKey(tbl_userregistration,on_delete=models.CASCADE)

class tbl_commant(models.Model):
    post = models.ForeignKey(tbl_post,on_delete=models.CASCADE)
    user = models.ForeignKey(tbl_userregistration,on_delete=models.CASCADE)
    comment_content = models.CharField(max_length=100)