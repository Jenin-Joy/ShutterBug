# Generated by Django 5.0.1 on 2024-02-20 12:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Guest', '0021_tbl_post_tbl_addgallery'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_modelpic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_image', models.FileField(upload_to='Assets/Model/Model_Pic/')),
                ('post_caption', models.CharField(max_length=30)),
                ('model_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Guest.tbl_modelregistration')),
            ],
        ),
    ]