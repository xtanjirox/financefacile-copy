# Generated by Django 5.0.6 on 2024-07-17 18:55

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0015_alter_financeentry_entry_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='financeentry',
            name='entry_date',
            field=models.DateField(default=datetime.datetime(2024, 7, 17, 18, 55, 20, 689126, tzinfo=datetime.timezone.utc)),
        ),
    ]