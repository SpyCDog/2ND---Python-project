# Generated by Django 4.2.4 on 2023-08-14 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("oz_pro", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="lead",
            name="id",
        ),
        migrations.AddField(
            model_name="lead",
            name="ID",
            field=models.AutoField(default=1, primary_key=True, serialize=False),
            preserve_default=False,
        ),
    ]
