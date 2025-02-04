# Generated by Django 5.0.2 on 2025-02-04 17:50

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cryptocoins',
            name='contracts',
        ),
        migrations.AddField(
            model_name='contract',
            name='crypto_coin',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Main.cryptocoins'),
        ),
    ]
