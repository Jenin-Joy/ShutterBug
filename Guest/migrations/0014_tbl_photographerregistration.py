# Generated by Django 5.0.1 on 2024-02-08 16:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0005_tbl_place_tbl_subcategory'),
        ('Guest', '0013_delete_tbl_photographerregistration'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_photographerregistration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photographer_name', models.CharField(max_length=30)),
                ('photographer_contact', models.CharField(max_length=30)),
                ('photographer_email', models.CharField(max_length=30)),
                ('photographer_address', models.CharField(max_length=30)),
                ('photographer_gender', models.CharField(max_length=30)),
                ('photographer_username', models.CharField(max_length=30)),
                ('photographer_photo', models.FileField(upload_to='Assets/Photographer/Photographer_photo/')),
                ('photographer_proof', models.FileField(upload_to='Assets/Photographer/Photographer_proof/')),
                ('photographer_active', models.CharField(max_length=30)),
                ('photographer_password', models.CharField(max_length=30)),
                ('photographer_category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Admin.tbl_category')),
                ('photographer_place', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Admin.tbl_place')),
            ],
        ),
    ]
