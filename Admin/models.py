from django.db import models

# Create your models here.

class tbl_district(models.Model):
    district_name = models.CharField(max_length=30)

class tbl_category(models.Model):
    category_name = models.CharField(max_length=30)

class tbl_admin(models.Model):
    admin_name = models.CharField(max_length=30)
    admin_contact = models.CharField(max_length=30)
    admin_email = models.CharField(max_length=30)
    admin_password = models.CharField(max_length=30)

class tbl_place(models.Model):
    district_id = models.ForeignKey(tbl_district,on_delete=models.CASCADE)
    place_name = models.CharField(max_length=30)    

class tbl_subcategory(models.Model):
    category_id = models.ForeignKey(tbl_category,on_delete=models.CASCADE)
    subcategory_name = models.CharField(max_length=30)     

class tbl_pcategory(models.Model):
    pcategory_name = models.CharField(max_length=30)

class tbl_ecategory(models.Model):
    ecategory_name = models.CharField(max_length=30)    
