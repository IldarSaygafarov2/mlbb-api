# Generated by Django 5.2.3 on 2025-06-16 10:45

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emblems', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emblem',
            name='id',
            field=models.UUIDField(default=uuid.UUID('f03f2a79-dcd4-40d6-bc14-a5bdda835985'), editable=False, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
