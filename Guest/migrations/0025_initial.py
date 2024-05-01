# Generated by Django 5.0.1 on 2024-02-24 13:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Admin', '0007_tbl_ecategory'),
        ('Guest', '0024_remove_tbl_complaint_editor_id_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_editorregistration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('editor_name', models.CharField(max_length=30)),
                ('editor_email', models.CharField(max_length=30)),
                ('editor_contact', models.CharField(max_length=30)),
                ('editor_address', models.CharField(max_length=30)),
                ('editor_photo', models.FileField(upload_to='Assets/Editor/Editor_photo/')),
                ('editor_proof', models.FileField(upload_to='Assets/Editor/Editor_proof/')),
                ('editor_username', models.CharField(max_length=30)),
                ('editor_active', models.CharField(max_length=30)),
                ('editor_gender', models.CharField(max_length=30)),
                ('editor_password', models.CharField(max_length=30)),
                ('editor_cpassword', models.CharField(max_length=30)),
                ('editor_status', models.IntegerField(default=0)),
                ('editor_doj', models.DateField(auto_now_add=True)),
                ('editor_category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Admin.tbl_ecategory')),
                ('editor_place', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Admin.tbl_place')),
            ],
        ),
        migrations.CreateModel(
            name='tbl_modelregistration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model_name', models.CharField(max_length=30)),
                ('model_contact', models.CharField(max_length=30)),
                ('model_email', models.CharField(max_length=30)),
                ('model_address', models.CharField(max_length=30)),
                ('model_gender', models.CharField(max_length=30)),
                ('model_photo', models.FileField(upload_to='Assets/Model/Model_photo/')),
                ('model_proof', models.FileField(upload_to='Assets/Model/Model_proof/')),
                ('model_password', models.CharField(max_length=30)),
                ('model_cpassword', models.CharField(max_length=30)),
                ('model_status', models.IntegerField(default=0)),
                ('model_doj', models.DateField(auto_now_add=True)),
                ('model_place', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Admin.tbl_place')),
            ],
        ),
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
                ('photographer_cpassword', models.CharField(max_length=30)),
                ('photographer_status', models.IntegerField(default=0)),
                ('photographer_doj', models.DateField(auto_now_add=True)),
                ('photographer_category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Admin.tbl_pcategory')),
                ('photographer_place', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Admin.tbl_place')),
            ],
        ),
        migrations.CreateModel(
            name='tbl_post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_title', models.CharField(max_length=30)),
                ('post_image', models.FileField(upload_to='Assets/Guest/Post_Image/')),
                ('post_caption', models.CharField(max_length=30)),
                ('paid_status', models.CharField(max_length=30)),
                ('post_amount', models.CharField(max_length=30)),
                ('p_status', models.CharField(max_length=30)),
                ('editor_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Guest.tbl_editorregistration')),
                ('photographer_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Guest.tbl_photographerregistration')),
            ],
        ),
        migrations.CreateModel(
            name='tbl_addgallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('addgallery_id', models.CharField(max_length=30)),
                ('addgallery_caption', models.CharField(max_length=30)),
                ('addgallery_image', models.FileField(upload_to='Assets/Guest/Add_Gallery/')),
                ('p_status', models.CharField(max_length=30)),
                ('post_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Guest.tbl_post')),
            ],
        ),
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
                ('user_cpassword', models.CharField(max_length=30)),
                ('user_status', models.IntegerField(default=0)),
                ('user_doj', models.DateField(auto_now_add=True)),
                ('user_place', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Admin.tbl_place')),
            ],
        ),
        migrations.CreateModel(
            name='tbl_feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feedback_description', models.CharField(max_length=30)),
                ('feedback_date', models.DateField(auto_now_add=True)),
                ('editor_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Guest.tbl_editorregistration')),
                ('model_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Guest.tbl_modelregistration')),
                ('photographer_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Guest.tbl_photographerregistration')),
                ('user_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Guest.tbl_userregistration')),
            ],
        ),
        migrations.CreateModel(
            name='tbl_complaint',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('complaint_title', models.CharField(max_length=30)),
                ('complaint_date', models.DateField(auto_now_add=True)),
                ('complaint_reply', models.CharField(max_length=30)),
                ('complaint_status', models.IntegerField(default=0)),
                ('complaint_description', models.CharField(max_length=30)),
                ('editor_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Guest.tbl_editorregistration')),
                ('model_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Guest.tbl_modelregistration')),
                ('photographer_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Guest.tbl_photographerregistration')),
                ('user_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Guest.tbl_userregistration')),
            ],
        ),
    ]
