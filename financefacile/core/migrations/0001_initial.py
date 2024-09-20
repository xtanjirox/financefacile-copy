# Generated by Django 5.0.6 on 2024-08-15 19:58

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EntryCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_title', models.CharField(max_length=50)),
                ('finance_entry_type', models.IntegerField(choices=[(1, 'DEPENSE'), (2, 'REVENUE')])),
            ],
            options={
                'verbose_name_plural': 'categories',
                'db_table': 'entry_category',
            },
        ),
        migrations.CreateModel(
            name='SeasonEntry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('season_name', models.CharField(max_length=50)),
                ('season_start', models.DateField()),
                ('season_end', models.DateField()),
            ],
            options={
                'verbose_name_plural': 'seasons',
                'db_table': 'season_entry',
            },
        ),
        migrations.CreateModel(
            name='FinanceEntry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('finance_entry_type', models.IntegerField(choices=[(1, 'DEPENSE'), (2, 'REVENUE')])),
                ('entry_value', models.FloatField(default=0)),
                ('entry_label', models.CharField(max_length=20)),
                ('entry_date', models.DateField(default=datetime.datetime(2024, 8, 15, 19, 58, 12, 267018, tzinfo=datetime.timezone.utc))),
                ('entry_category', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='core.entrycategory')),
                ('season', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='core.seasonentry')),
            ],
            options={
                'verbose_name_plural': 'entries',
                'db_table': 'finance_entries',
            },
        ),
    ]
