# Generated by Django 4.2 on 2024-11-11 20:15

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("project_functionality", "0005_alter_helppoint_name"),
    ]

    operations = [
        migrations.AlterField(
            model_name="helppoint",
            name="name",
            field=models.TextField(blank=True, default=None, null=True),
        ),
    ]
