# Generated by Django 2.1.4 on 2018-12-17 18:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import user.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=500)),
                ('is_default', models.BooleanField(default=True)),
                ('available_from', models.DateTimeField(default=user.models.default_start_time)),
                ('available_to', models.DateTimeField(default=user.models.default_end_time)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'user_address',
            },
        ),
    ]
