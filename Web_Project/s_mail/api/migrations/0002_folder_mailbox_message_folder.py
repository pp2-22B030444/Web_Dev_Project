# Generated by Django 5.0.3 on 2024-04-22 08:38

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='folder',
            name='mailbox',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='api.mailbox'),
        ),
        migrations.AddField(
            model_name='message',
            name='folder',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='api.folder'),
        ),
    ]
