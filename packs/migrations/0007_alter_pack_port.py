# Generated by Django 4.1.7 on 2023-03-03 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('packs', '0006_pack_port_alter_pack_linux_password_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pack',
            name='port',
            field=models.IntegerField(default=0),
        ),
    ]
