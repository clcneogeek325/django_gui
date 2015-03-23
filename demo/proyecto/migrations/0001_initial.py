# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='campo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=100, blank=True)),
                ('tipo', models.CharField(blank=True, max_length=100, choices=[(b'CharField', b'CHAR'), (b'IntegerField', b'INT'), (b'BooleanField', b'BOOLEAN'), (b'BigIntegerField', b'BIG_INTEGER'), (b'BooleanField', b'BOOLEAN')])),
                ('longitud', models.FloatField(default=100)),
                ('null', models.BooleanField(default=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='configuracion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tiene_static', models.BooleanField(default=True)),
                ('tiene_media', models.BooleanField(default=True)),
                ('url_static', models.CharField(default=b'static', max_length=100, blank=True)),
                ('url_media', models.CharField(default=b'media', max_length=100, blank=True)),
                ('campo', models.ManyToManyField(to='proyecto.campo')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='proyecto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=100, blank=True)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='tabla',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=100, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='configuracion',
            name='proyecto',
            field=models.ForeignKey(to='proyecto.proyecto', unique=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='configuracion',
            name='tabla',
            field=models.ManyToManyField(to='proyecto.tabla'),
            preserve_default=True,
        ),
    ]
