# Generated by Django 5.1 on 2025-01-20 17:54

import arrow.api
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0005_remove_servicerequest_created_at"),
    ]

    operations = [
        migrations.AddField(
            model_name="servicerequest",
            name="created_at",
            field=models.DateTimeField(default=arrow.api.now),
        ),
    ]
