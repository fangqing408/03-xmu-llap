# Generated by Django 4.2.7 on 2025-04-13 07:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("xmu", "0013_alter_backgroundimage_author_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="backgroundimage",
            name="author",
            field=models.CharField(
                blank=True, default="Isaac Newton", max_length=100, null=True
            ),
        ),
    ]
