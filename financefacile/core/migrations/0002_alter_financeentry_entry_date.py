# Generated by Django 5.0.6 on 2024-08-15 20:03

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='financeentry',
            name='entry_date',
            field=models.DateField(default=datetime.datetime(2024, 8, 15, 20, 3, 6, 631795, tzinfo=datetime.timezone.utc)),
        ),
    ]
