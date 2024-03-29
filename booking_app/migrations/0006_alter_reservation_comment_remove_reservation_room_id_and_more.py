# Generated by Django 5.0.2 on 2024-02-19 01:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("booking_app", "0005_room_projector"),
    ]

    operations = [
        migrations.AlterField(
            model_name="reservation",
            name="comment",
            field=models.TextField(),
        ),
        migrations.RemoveField(
            model_name="reservation",
            name="room_id",
        ),
        migrations.AddField(
            model_name="reservation",
            name="room_id",
            field=models.ManyToManyField(to="booking_app.room"),
        ),
    ]
