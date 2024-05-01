# Generated by Django 5.0.1 on 2024-02-14 06:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Guest', '0015_tbl_userregistration'),
    ]

    operations = [
        migrations.AddField(
            model_name='tbl_editorregistration',
            name='editor_status',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='tbl_photographerregistration',
            name='photographer_status',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='tbl_userregistration',
            name='user_status',
            field=models.IntegerField(default=0),
        ),
    ]
