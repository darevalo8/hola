# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('fields', models.FileField(upload_to='archivos/')),
            ],
        ),
        migrations.CreateModel(
            name='Comunity',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Nota',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('puntuacion', models.IntegerField()),
                ('total', models.IntegerField()),
                ('activities', models.ForeignKey(to='conquers.Activity')),
                ('comunity', models.ForeignKey(to='conquers.Comunity')),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('type_user', models.IntegerField(default=1, choices=[(1, 'Presidente'), (2, 'Auditor')])),
                ('comunity', models.ForeignKey(to='conquers.Comunity')),
                ('nickname', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='activity',
            name='comunity',
            field=models.ForeignKey(to='conquers.Comunity'),
        ),
    ]
