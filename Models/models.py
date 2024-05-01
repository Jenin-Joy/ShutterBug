from django.db import models
from Guest.models import *

# Create your models here.


class tbl_modelpost(models.Model):
      post_image = models.FileField(upload_to='Assets/Model/Model_Post/')
      post_caption = models.CharField(max_length=30)
      model_id = models.ForeignKey(tbl_modelregistration,on_delete=models.CASCADE,null=True) 

class tbl_modelpic(models.Model):
      modelpost_id = models.ForeignKey(tbl_modelpost,on_delete=models.CASCADE,null=True)
      modelpost_image = models.FileField(upload_to='Assets/Model/ModelPost_Image/')

     

