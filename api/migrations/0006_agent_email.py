# Generated by Django 5.1.6 on 2025-03-31 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0005_property_details_property_distance_between_delhi_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="agent",
            name="email",
            field=models.CharField(blank=True, default=None, max_length=200, null=True),
        ),
    ]
