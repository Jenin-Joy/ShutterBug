# Generated by Django 5.0.1 on 2024-02-28 08:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0008_alter_tbl_photographerbooking_booking_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tbl_photographerbooking',
            name='payment_amount',
            field=models.IntegerField(default=0),
        ),
    ]
