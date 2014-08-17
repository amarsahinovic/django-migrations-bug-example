# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('galleries', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='galleryitem',
            name='article',
            field=models.ForeignKey(to='articles.Article', blank=True, null=True),
            preserve_default=True,
        ),
    ]
