# Generated by Django 5.0.6 on 2024-07-08 22:36

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
            field=models.DateField(default=datetime.datetime(2024, 7, 8, 22, 36, 36, 655155, tzinfo=datetime.timezone.utc)),
        ),
    ]
