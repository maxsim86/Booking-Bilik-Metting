# Generated by Django 5.0.2 on 2024-02-15 03:40

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0002_booking_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='time_ordered',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
    ]