# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blight_app', '0008_link_vote'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='link',
            name='submitter',
        ),
        migrations.RemoveField(
            model_name='vote',
            name='link',
        ),
        migrations.DeleteModel(
            name='Link',
        ),
        migrations.RemoveField(
            model_name='vote',
            name='voter',
        ),
        migrations.DeleteModel(
            name='Vote',
        ),
    ]
