# Generated by Django 5.1.6 on 2025-04-07 05:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0008_remove_property_price_range_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="property",
            name="price_range",
            field=models.CharField(blank=True, default=None, max_length=120, null=True),
        ),
        migrations.AddField(
            model_name="property",
            name="road_width_filter",
            field=models.CharField(blank=True, default=None, max_length=120, null=True),
        ),
        migrations.AddField(
            model_name="property",
            name="size_range",
            field=models.CharField(blank=True, default=None, max_length=120, null=True),
        ),
    ]
