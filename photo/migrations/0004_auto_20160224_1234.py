# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('photo', '0003_auto_20160223_1228'),
    ]

    operations = [
        migrations.RenameField(
            model_name='photo',
            old_name='tags_list',
            new_name='tags',
        ),
    ]
