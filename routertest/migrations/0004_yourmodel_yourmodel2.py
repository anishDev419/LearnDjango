# Generated by Django 5.0.4 on 2024-05-10 12:05

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('routertest', '0003_instance'),
    ]

    operations = [
        migrations.AddField(
            model_name='yourmodel',
            name='yourmodel2',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='routertest.yourmodel2'),
        ),
    ]
