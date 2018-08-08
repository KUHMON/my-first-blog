# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='comentario',
            field=models.CharField(max_length=200, default=datetime.datetime(2018, 8, 8, 19, 35, 42, 32596, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
