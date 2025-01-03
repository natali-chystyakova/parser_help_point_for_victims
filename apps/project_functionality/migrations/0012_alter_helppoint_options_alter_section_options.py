# Generated by Django 5.1.4 on 2024-12-30 18:04

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("project_functionality", "0011_rename_section_helppoint_sect"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="helppoint",
            options={"ordering": ["id"]},
        ),
        migrations.AlterModelOptions(
            name="section",
            options={
                "ordering": ["pk"],
                "verbose_name": "section for points",
                "verbose_name_plural": "sections for points",
            },
        ),
    ]