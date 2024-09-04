# Generated by Django 5.1 on 2024-09-03 23:50

import datetime
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='PostModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_post', models.CharField(max_length=100)),
                ('txt_post', models.CharField(max_length=10000000)),
                ('date', models.DateTimeField(verbose_name=datetime.datetime(2024, 9, 3, 20, 50, 52, 66738))),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
