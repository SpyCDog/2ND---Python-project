# Generated by Django 4.2.4 on 2023-08-14 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("oz_pro", "0002_remove_lead_id_lead_id"),
    ]

    operations = [
        migrations.AddField(
            model_name="lead",
            name="delete_image",
            field=models.ImageField(default="delete.png", upload_to="static"),
        ),
        migrations.AddField(
            model_name="lead",
            name="image",
            field=models.ImageField(default="anonymous.png", upload_to="static"),
        ),
    ]
