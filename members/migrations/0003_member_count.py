# Generated by Django 4.2.5 on 2024-03-27 06:04

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("members", "0002_member_joined_date_member_phone"),
    ]

    operations = [
        migrations.AddField(
            model_name="member",
            name="count",
            field=models.IntegerField(null=True),
        ),
    ]