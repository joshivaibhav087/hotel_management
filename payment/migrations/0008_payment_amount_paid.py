# Generated by Django 3.1.3 on 2021-03-08 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0007_auto_20210308_1336'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='amount_paid',
            field=models.IntegerField(default=1),
        ),
    ]
