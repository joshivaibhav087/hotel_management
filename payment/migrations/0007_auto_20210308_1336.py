# Generated by Django 3.1.3 on 2021-03-08 08:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0006_payment_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='payment',
            old_name='patment_mode',
            new_name='payment_mode',
        ),
    ]