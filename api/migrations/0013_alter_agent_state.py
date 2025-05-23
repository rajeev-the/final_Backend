# Generated by Django 5.1.6 on 2025-04-07 06:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0012_alter_property_state"),
    ]

    operations = [
        migrations.AlterField(
            model_name="agent",
            name="state",
            field=models.CharField(
                blank=True,
                choices=[
                    ("Haryana", "Haryana"),
                    ("Delhi", "Delhi"),
                    ("Punjab", "Punjab"),
                    ("Uttar Pradesh", "Uttar_Pradesh"),
                ],
                default=None,
                max_length=20,
                null=True,
            ),
        ),
    ]
