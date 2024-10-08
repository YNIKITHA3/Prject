# Generated by Django 5.0.6 on 2024-08-24 10:23

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("dashboard", "0002_alter_notes_options_homework"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name="homework",
            name="due",
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="homework",
            name="subject",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name="homework",
            name="title",
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name="homework",
            name="user",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
