# Generated by Django 5.0.1 on 2024-02-16 12:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Guest', '0019_rename_post_name_tbl_post_post_title'),
    ]

    operations = [
        migrations.DeleteModel(
            name='tbl_post',
        ),
    ]