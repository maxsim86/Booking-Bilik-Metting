# Generated by Django 5.0.2 on 2024-02-19 01:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        (
            "booking_app",
            "0006_alter_reservation_comment_remove_reservation_room_id_and_more",
        ),
    ]

    operations = [
        migrations.RenameField(
            model_name="reservation",
            old_name="room_id",
            new_name="room",
        ),
    ]