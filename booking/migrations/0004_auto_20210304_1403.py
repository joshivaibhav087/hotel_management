# Generated by Django 3.1.3 on 2021-03-04 08:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0003_remove_booking_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='bed_type',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='booking',
            name='food',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='booking',
            name='room_type',
            field=models.CharField(max_length=20),
        ),
    ]