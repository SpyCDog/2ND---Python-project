# Generated by Django 4.2.4 on 2023-08-14 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("oz_pro", "0003_lead_delete_image_lead_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="lead",
            name="image",
            field=models.ImageField(default="anonymous.jpg", upload_to="static"),
        ),
    ]
