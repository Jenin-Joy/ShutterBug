# Generated by Django 5.0.1 on 2024-02-12 05:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0006_tbl_pcategory'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_ecategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ecategory_name', models.CharField(max_length=30)),
            ],
        ),
    ]