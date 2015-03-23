# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('proyecto', '0002_remove_configuracion_campo'),
    ]

    operations = [
        migrations.AddField(
            model_name='tabla',
            name='campo',
            field=models.ManyToManyField(to='proyecto.campo'),
            preserve_default=True,
        ),
    ]
