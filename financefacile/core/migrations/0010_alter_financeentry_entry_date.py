# Generated by Django 5.0.6 on 2024-07-15 23:25

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_alter_financeentry_entry_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='financeentry',
            name='entry_date',
            field=models.DateField(default=datetime.datetime(2024, 7, 15, 23, 25, 41, 502732, tzinfo=datetime.timezone.utc)),
        ),
    ]