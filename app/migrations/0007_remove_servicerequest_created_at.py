# Generated by Django 5.1 on 2025-01-20 17:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0006_servicerequest_created_at"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="servicerequest",
            name="created_at",
        ),
    ]
