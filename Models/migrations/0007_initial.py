# Generated by Django 5.0.1 on 2024-02-28 05:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Guest', '0029_tbl_addgallery'),
        ('Models', '0006_delete_tbl_modelpic'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_modelpost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_image', models.FileField(upload_to='Assets/Model/Model_Post/')),
                ('post_caption', models.CharField(max_length=30)),
                ('model_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Guest.tbl_modelregistration')),
            ],
        ),
        migrations.CreateModel(
            name='tbl_modelpic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('modelpost_image', models.FileField(upload_to='Assets/Model/ModelPost_Image/')),
                ('modelpost_caption', models.CharField(max_length=30)),
                ('modelpost_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Models.tbl_modelpost')),
            ],
        ),
    ]
