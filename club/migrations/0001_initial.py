# Generated by Django 4.0.4 on 2022-04-15 20:14

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
            name='Meeting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('meetingTitle', models.CharField(max_length=255)),
                ('meetingDate', models.DateField()),
                ('meetingTime', models.TimeField()),
                ('location', models.CharField(max_length=255)),
                ('agenda', models.TextField()),
            ],
            options={
                'verbose_name_plural': 'meetings',
                'db_table': 'meeting',
            },
        ),
        migrations.CreateModel(
            name='Resources',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resourceName', models.CharField(max_length=255)),
                ('resourceType', models.CharField(max_length=255)),
                ('url', models.URLField()),
                ('dateEntered', models.DateField()),
                ('description', models.TextField()),
                ('userID', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'resources',
                'db_table': 'resources',
            },
        ),
        migrations.CreateModel(
            name='MeetingMinutes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('minutesText', models.TextField()),
                ('attendance', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
                ('meetingID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='club.meeting')),
            ],
            options={
                'db_table': 'meetingMinutes',
            },
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eventTitle', models.CharField(max_length=255)),
                ('location', models.CharField(max_length=255)),
                ('eventDate', models.DateField()),
                ('eventTime', models.TimeField()),
                ('description', models.TextField()),
                ('userID', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'events',
                'db_table': 'event',
            },
        ),
    ]