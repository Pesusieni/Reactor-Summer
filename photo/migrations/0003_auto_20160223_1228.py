# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('photo', '0002_auto_20160218_1815'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='photo',
            name='tags',
        ),
        migrations.AddField(
            model_name='photo',
            name='tags_list',
            field=models.ManyToManyField(to='photo.Tag', blank=True),
            preserve_default=True,
        ),
    ]
