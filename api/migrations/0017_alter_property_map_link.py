# Generated by Django 5.1.6 on 2025-04-10 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0016_alter_property_map_link"),
    ]

    operations = [
        migrations.AlterField(
            model_name="property",
            name="map_link",
            field=models.TextField(
                default="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d42157498.47345266!2d60.94156072887267!3d19.69240573692257!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x30635ff5d23cbb0f%3A0xe1b092d74e10e9c5!2sIndia!5e0!3m2!1sen!2sin!4v1744037809273!5m2!1sen!2sin",
                max_length=2000,
            ),
        ),
    ]
