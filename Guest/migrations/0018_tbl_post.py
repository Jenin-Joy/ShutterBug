# Generated by Django 5.0.1 on 2024-02-16 11:10

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Guest', '0017_alter_tbl_editorregistration_editor_category_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_id', models.CharField(max_length=30)),
                ('post_name', models.CharField(max_length=30)),
                ('post_image', models.FileField(upload_to='Assets/Guest/Post_Image/')),
                ('post_caption', models.CharField(max_length=30)),
                ('post_amount', models.CharField(max_length=30)),
                ('paid_status', models.CharField(max_length=30)),
                ('editor_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Guest.tbl_editorregistration')),
                ('photographer_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Guest.tbl_photographerregistration')),
            ],
        ),
    ]
