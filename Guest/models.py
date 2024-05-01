from django.db import models
from Admin.models import *
# Create your models here.

class tbl_editorregistration(models.Model):
    editor_name = models.CharField(max_length=30)
    editor_email = models.CharField(max_length=30)
    editor_contact = models.CharField(max_length=30)
    editor_address = models.CharField(max_length=30)
    editor_photo = models.FileField(upload_to='Assets/Editor/Editor_photo/')
    editor_proof = models.FileField(upload_to='Assets/Editor/Editor_proof/')
    editor_username = models.CharField(max_length=30)
    editor_active = models.CharField(max_length=30)
    editor_gender = models.CharField(max_length=30)
    editor_place = models.ForeignKey(tbl_place,on_delete=models.CASCADE,null=True)
    editor_password = models.CharField(max_length=30)
    editor_cpassword = models.CharField(max_length=30)
    editor_category = models.ForeignKey(tbl_ecategory,on_delete=models.CASCADE,null=True)
    editor_status = models.IntegerField(default=0)
    editor_doj = models.DateField(auto_now_add=True)

class tbl_photographerregistration(models.Model):
    photographer_name = models.CharField(max_length=30)
    photographer_contact = models.CharField(max_length=30)
    photographer_email = models.CharField(max_length=30)    
    photographer_address = models.CharField(max_length=30)
    photographer_gender = models.CharField(max_length=30)
    photographer_username = models.CharField(max_length=30)
    photographer_photo = models.FileField(upload_to='Assets/Photographer/Photographer_photo/')
    photographer_proof = models.FileField(upload_to='Assets/Photographer/Photographer_proof/')    
    photographer_active = models.CharField(max_length=30)    
    photographer_place = models.ForeignKey(tbl_place,on_delete=models.CASCADE,null=True)    
    photographer_category = models.ForeignKey(tbl_pcategory,on_delete=models.CASCADE,null=True) 
    photographer_password = models.CharField(max_length=30)  
    photographer_cpassword = models.CharField(max_length=30)
    photographer_status = models.IntegerField(default=0)
    photographer_doj = models.DateField(auto_now_add=True) 


class tbl_userregistration(models.Model):
    user_name = models.CharField(max_length=30)
    user_contact = models.CharField(max_length=30)
    user_email = models.CharField(max_length=30)
    user_gender = models.CharField(max_length=30)    
    user_address = models.CharField(max_length=30)
    user_photo = models.FileField(upload_to='Assets/User/User_photo/')     
    user_username = models.CharField(max_length=30)       
    user_active = models.CharField(max_length=30)    
    user_place = models.ForeignKey(tbl_place,on_delete=models.CASCADE,null=True)    
    user_password = models.CharField(max_length=30)    
    user_cpassword = models.CharField(max_length=30)  
    user_status = models.IntegerField(default=0) 
    user_doj = models.DateField(auto_now_add=True)

class tbl_modelregistration(models.Model):
    model_name = models.CharField(max_length=30)
    model_contact = models.CharField(max_length=30)
    model_email = models.CharField(max_length=30)
    model_address = models.CharField(max_length=30)
    model_gender = models.CharField(max_length=30)
    model_place = models.ForeignKey(tbl_place,on_delete=models.CASCADE,null=True)
    model_photo = models.FileField(upload_to='Assets/Model/Model_photo/')
    model_proof = models.FileField(upload_to='Assets/Model/Model_proof/')
    model_password = models.CharField(max_length=30)
    model_cpassword = models.CharField(max_length=30)
    model_status = models.IntegerField(default=0)
    model_doj = models.DateField(auto_now_add=True)    

class tbl_post(models.Model):
      post_title = models.CharField(max_length=30)
      post_image = models.FileField(upload_to='Assets/Guest/Post_Image/')
      post_caption = models.CharField(max_length=30)
      paid_status = models.CharField(max_length=30)
      post_amount = models.CharField(max_length=30)  
      editor_id = models.ForeignKey(tbl_editorregistration,on_delete=models.CASCADE,null=True)
      photographer_id = models.ForeignKey(tbl_photographerregistration,on_delete=models.CASCADE,null=True)
      p_status =  models.CharField(max_length=30) 

class tbl_addgallery(models.Model):
      addgallery_caption = models.CharField(max_length=30)
      addgallery_image = models.FileField(upload_to='Assets/Guest/Add_Gallery/')
      post_id = models.ForeignKey(tbl_post,on_delete=models.CASCADE,null=True)
      p_status =  models.CharField(max_length=30)


class tbl_complaint(models.Model):
      complaint_title = models.CharField(max_length=30)
      complaint_date=models.DateField(auto_now_add=True)
      complaint_reply = models.CharField(max_length=30)
      complaint_status = models.IntegerField(default=0)
      user_id = models.ForeignKey(tbl_userregistration,on_delete=models.CASCADE,null=True)
      editor_id = models.ForeignKey(tbl_editorregistration,on_delete=models.CASCADE,null=True)
      photographer_id = models.ForeignKey(tbl_photographerregistration,on_delete=models.CASCADE,null=True)
      model_id = models.ForeignKey(tbl_modelregistration,on_delete=models.CASCADE,null=True)
      complaint_description = models.CharField(max_length=30)  


class tbl_feedback(models.Model):
      feedback_description = models.CharField(max_length=30)
      feedback_date=models.DateField(auto_now_add=True)
      user_id = models.ForeignKey(tbl_userregistration,on_delete=models.CASCADE,null=True) 
      editor_id = models.ForeignKey(tbl_editorregistration,on_delete=models.CASCADE,null=True) 
      photographer_id = models.ForeignKey(tbl_photographerregistration,on_delete=models.CASCADE,null=True) 
      model_id = models.ForeignKey(tbl_modelregistration,on_delete=models.CASCADE,null=True) 


class tbl_chat(models.Model):
    chat_content = models.CharField(max_length=500)
    chat_time = models.DateTimeField()
    chat_file = models.FileField(upload_to='ChatFiles/')
    user_from = models.ForeignKey(tbl_userregistration,on_delete=models.CASCADE,related_name="user_from",null=True)
    user_to = models.ForeignKey(tbl_userregistration,on_delete=models.CASCADE,related_name="user_to",null=True)
    photographer_to = models.ForeignKey(tbl_photographerregistration,on_delete=models.CASCADE,related_name="photographer_to",null=True)
    photographer_from = models.ForeignKey(tbl_photographerregistration,on_delete=models.CASCADE,related_name="photographer_from",null=True)


class tbl_epchat(models.Model):
    chat_content = models.CharField(max_length=500)
    chat_time = models.DateTimeField()
    chat_file = models.FileField(upload_to='ChatFiles/')
    editor_from = models.ForeignKey(tbl_editorregistration,on_delete=models.CASCADE,related_name="editor_from",null=True)
    editor_to = models.ForeignKey(tbl_editorregistration,on_delete=models.CASCADE,related_name="editor_to",null=True)
    photographer_to = models.ForeignKey(tbl_photographerregistration,on_delete=models.CASCADE,related_name="photographers_to",null=True)
    photographer_from = models.ForeignKey(tbl_photographerregistration,on_delete=models.CASCADE,related_name="photographers_from",null=True)

class tbl_mpchat(models.Model):
    chat_content = models.CharField(max_length=500)
    chat_time = models.DateTimeField()
    chat_file = models.FileField(upload_to='ChatFiles/')
    model_from = models.ForeignKey(tbl_modelregistration,on_delete=models.CASCADE,related_name="model_from",null=True)
    model_to = models.ForeignKey(tbl_modelregistration,on_delete=models.CASCADE,related_name="model_to",null=True)
    photographer_to = models.ForeignKey(tbl_photographerregistration,on_delete=models.CASCADE,related_name="photographerss_to",null=True)
    photographer_from = models.ForeignKey(tbl_photographerregistration,on_delete=models.CASCADE,related_name="photographerss_from",null=True)    
