# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('proyecto', '0003_tabla_campo'),
    ]

    operations = [
        migrations.AddField(
            model_name='proyecto',
            name='fecha_creacion',
            field=models.DateTimeField(default=datetime.datetime.now, blank=True),
            preserve_default=True,
        ),
    ]
