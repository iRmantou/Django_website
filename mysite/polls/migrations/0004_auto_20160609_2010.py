# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_teacherselect'),
    ]

    operations = [
        migrations.AddField(
            model_name='gradeoneselectt',
            name='average1',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='gradethreeselect',
            name='average3',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='gradetwoselect',
            name='average2',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='teacherselect',
            name='average4',
            field=models.IntegerField(default=0),
        ),
    ]
