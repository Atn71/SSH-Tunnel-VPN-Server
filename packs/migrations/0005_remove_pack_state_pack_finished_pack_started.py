# Generated by Django 4.1.7 on 2023-03-03 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('packs', '0004_pack_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pack',
            name='state',
        ),
        migrations.AddField(
            model_name='pack',
            name='finished',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='pack',
            name='started',
            field=models.BooleanField(default=False),
        ),
    ]
