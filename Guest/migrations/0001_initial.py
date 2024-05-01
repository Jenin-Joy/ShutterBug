# Generated by Django 5.0.1 on 2024-02-06 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_modelregistration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model_name', models.CharField(max_length=30)),
                ('model_contact', models.CharField(max_length=30)),
                ('model_email', models.CharField(max_length=30)),
                ('model_address', models.CharField(max_length=30)),
                ('model_gender', models.CharField(max_length=30)),
                ('model_district', models.CharField(max_length=30)),
                ('model_place', models.CharField(max_length=30)),
                ('model_photo', models.CharField(max_length=30)),
                ('model_proof', models.CharField(max_length=30)),
                ('model_password', models.CharField(max_length=30)),
                ('model_confirmpassword', models.CharField(max_length=30)),
            ],
        ),
    ]