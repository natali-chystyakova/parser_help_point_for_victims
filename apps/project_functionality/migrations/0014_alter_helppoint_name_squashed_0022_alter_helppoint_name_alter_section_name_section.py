# Generated by Django 4.2.9 on 2025-01-08 17:46

from django.db import migrations, models


class Migration(migrations.Migration):
    replaces = [
        ("project_functionality", "0014_alter_helppoint_name"),
        ("project_functionality", "0015_alter_helppoint_name"),
        ("project_functionality", "0016_alter_helppoint_link_alter_section_name_section"),
        ("project_functionality", "0017_alter_helppoint_link"),
        ("project_functionality", "0018_alter_helppoint_unique_together"),
        ("project_functionality", "0019_alter_section_name_section"),
        ("project_functionality", "0020_alter_helppoint_link"),
        ("project_functionality", "0021_alter_helppoint_link"),
        ("project_functionality", "0022_alter_helppoint_name_alter_section_name_section"),
    ]

    dependencies = [
        ("project_functionality", "0013_rename_information_helppoint_address_helppoint_link_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="helppoint",
            name="name",
            field=models.TextField(blank=True, default=None, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name="helppoint",
            name="name",
            field=models.TextField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name="helppoint",
            name="link",
            field=models.URLField(blank=True, default=None, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name="section",
            name="name_section",
            field=models.CharField(max_length=300),
        ),
        migrations.AlterField(
            model_name="helppoint",
            name="link",
            field=models.URLField(blank=True, default=None, null=True),
        ),
        migrations.AlterUniqueTogether(
            name="helppoint",
            unique_together={("name", "sect")},
        ),
        migrations.AlterField(
            model_name="section",
            name="name_section",
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name="helppoint",
            name="link",
            field=models.URLField(blank=True, default=None, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name="helppoint",
            name="link",
            field=models.TextField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name="helppoint",
            name="name",
            field=models.TextField(blank=True, default=None, max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name="section",
            name="name_section",
            field=models.CharField(max_length=300),
        ),
    ]
