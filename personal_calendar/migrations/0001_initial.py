# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-08 16:33
from __future__ import unicode_literals

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
            name='Evenement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=250, unique=True)),
                ('description', models.TextField()),
                ('date', models.DateTimeField()),
                ('lieu', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Evenement_Participant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.IntegerField(choices=[(0, 'hôte'), (1, 'invité'), (2, 'désisté')])),
                ('evenement', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='personal_calendar.Evenement')),
                ('participant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='evenement',
            name='participants',
            field=models.ManyToManyField(through='personal_calendar.Evenement_Participant', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterUniqueTogether(
            name='evenement_participant',
            unique_together=set([('evenement', 'participant')]),
        ),
    ]
