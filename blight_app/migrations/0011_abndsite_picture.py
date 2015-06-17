# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blight_app', '0010_userprofile'),
    ]

    operations = [
        migrations.AddField(
            model_name='abndsite',
            name='picture',
            field=models.ImageField(default=b'properties_images/default.png', upload_to=b'properties_images', blank=True),
            preserve_default=True,
        ),
    ]
