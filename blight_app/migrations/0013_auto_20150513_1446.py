# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blight_app', '0012_auto_20150513_1434'),
    ]

    operations = [
        migrations.AlterField(
            model_name='abndsite',
            name='picture',
            field=models.ImageField(default=b'/static/media/properties_images/default.png', max_length=512, null=b'True', upload_to=b'properties_images/', blank=True),
            preserve_default=True,
        ),
    ]
