# Generated by Django 4.2.1 on 2023-05-28 07:09

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="post",
            name="date",
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
