# Generated by Django 4.1.7 on 2023-03-27 22:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='WebhookReports',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField()),
                ('name', models.TextField(max_length=100)),
                ('dt', models.DateTimeField()),
                ('mail', models.TextField(max_length=100)),
                ('desc', models.TextField(blank=True, default='No desc', max_length=100, null=True)),
                ('phone_number', models.TextField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='PaymentRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idpay_id', models.CharField(blank=True, default='', max_length=100)),
                ('amount', models.IntegerField()),
                ('verified', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
