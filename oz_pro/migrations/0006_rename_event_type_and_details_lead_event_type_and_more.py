# Generated by Django 4.2.4 on 2023-08-16 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("oz_pro", "0005_alter_lead_image"),
    ]

    operations = [
        migrations.RenameField(
            model_name="lead",
            old_name="event_type_and_details",
            new_name="event_type",
        ),
        migrations.RemoveField(
            model_name="lead",
            name="delete_image",
        ),
        migrations.AlterField(
            model_name="lead",
            name="image",
            field=models.ImageField(default="Picture7.png", upload_to="static/pics"),
        ),
    ]