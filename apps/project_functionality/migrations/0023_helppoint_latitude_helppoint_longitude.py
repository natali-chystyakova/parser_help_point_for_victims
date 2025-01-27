# Generated by Django 4.2.9 on 2025-01-13 16:27

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        (
            "project_functionality",
            "0014_alter_helppoint_name_squashed_0022_alter_helppoint_name_alter_section_name_section",
        ),
    ]

    operations = [
        migrations.AddField(
            model_name="helppoint",
            name="latitude",
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="helppoint",
            name="longitude",
            field=models.FloatField(blank=True, null=True),
        ),
    ]
