# Generated by Django 4.1.7 on 2023-04-06 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('packs', '0008_alter_pack_port'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pack',
            name='linux_password',
            field=models.CharField(blank=True, default='', max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='pack',
            name='linux_username',
            field=models.CharField(blank=True, default='', max_length=10, null=True),
        ),
    ]
