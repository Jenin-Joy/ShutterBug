# Generated by Django 5.0.1 on 2024-02-08 16:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0005_tbl_place_tbl_subcategory'),
        ('Guest', '0014_tbl_photographerregistration'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_userregistration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=30)),
                ('user_contact', models.CharField(max_length=30)),
                ('user_email', models.CharField(max_length=30)),
                ('user_gender', models.CharField(max_length=30)),
                ('user_address', models.CharField(max_length=30)),
                ('user_photo', models.FileField(upload_to='Assets/User/User_photo/')),
                ('user_username', models.CharField(max_length=30)),
                ('user_active', models.CharField(max_length=30)),
                ('user_password', models.CharField(max_length=30)),
                ('user_place', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Admin.tbl_place')),
            ],
        ),
    ]
