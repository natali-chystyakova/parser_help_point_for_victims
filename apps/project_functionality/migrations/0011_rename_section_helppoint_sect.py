# Generated by Django 4.2 on 2024-12-10 16:15

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("project_functionality", "0010_alter_helppoint_information"),
    ]

    operations = [
        migrations.RenameField(
            model_name="helppoint",
            old_name="section",
            new_name="sect",
        ),
    ]