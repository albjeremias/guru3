# Generated by Django 4.1.13 on 2024-06-15 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("snom", "0002_alter_snomphone_id"),
    ]

    operations = [
        migrations.CreateModel(
            name="SnomFirmware",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "model",
                    models.CharField(max_length=16, verbose_name="Phone model name"),
                ),
                (
                    "download_url",
                    models.CharField(
                        max_length=512, verbose_name="Firmware download URI"
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="snomphone",
            name="no_firmware_update",
            field=models.BooleanField(
                blank=True,
                default=False,
                verbose_name="Do not push firmware updates to this phone.",
            ),
        ),
    ]
