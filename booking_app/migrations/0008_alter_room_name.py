# Generated by Django 5.0.2 on 2024-02-19 02:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("booking_app", "0007_rename_room_id_reservation_room"),
    ]

    operations = [
        migrations.AlterField(
            model_name="room",
            name="name",
            field=models.CharField(max_length=100),
        ),
    ]
