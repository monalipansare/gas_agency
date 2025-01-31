# Generated by Django 5.1 on 2025-01-20 17:46

import arrow.api
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0003_servicerequest_attachment_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="servicerequest",
            name="attachment",
        ),
        migrations.RemoveField(
            model_name="servicerequest",
            name="resolved_at",
        ),
        migrations.AddField(
            model_name="servicerequest",
            name="created_at",
            field=models.DateTimeField(default=arrow.api.now),
        ),
        migrations.AlterField(
            model_name="servicerequest",
            name="description",
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name="servicerequest",
            name="service_type",
            field=models.CharField(
                choices=[
                    ("Gas", "Gas Leakage"),
                    ("Gaspipeline", "Gas Pipeline Leakage"),
                    ("Cylinder", "Cylinder Nozzle Break"),
                    ("Billing", "Billing Issue"),
                ],
                max_length=100,
            ),
        ),
        migrations.AlterField(
            model_name="servicerequest",
            name="status",
            field=models.CharField(default="Pending", max_length=50),
        ),
    ]
