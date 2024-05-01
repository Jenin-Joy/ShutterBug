# Generated by Django 5.0.1 on 2024-02-24 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Photographers', '0007_delete_tbl_addgallery'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_addgallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('addgallery_image', models.FileField(upload_to='Assets/Photographer/AddGallery_image/')),
                ('addgallery_caption', models.CharField(max_length=30)),
            ],
        ),
    ]
