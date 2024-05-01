# Generated by Django 5.0.1 on 2024-02-16 12:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Guest', '0020_delete_tbl_post'),
    ]

    operations = [
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
    ]