# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0004_auto_20160609_2010'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gradeonechoice',
            name='sum1',
        ),
        migrations.RemoveField(
            model_name='gradethreechoice',
            name='sum3',
        ),
        migrations.RemoveField(
            model_name='gradetwochoice',
            name='sum2',
        ),
        migrations.RemoveField(
            model_name='teacherchoice',
            name='sum4',
        ),
        migrations.AddField(
            model_name='gradeoneselectt',
            name='sum1',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='gradethreeselect',
            name='sum3',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='gradetwoselect',
            name='sum2',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='teacherselect',
            name='sum4',
            field=models.IntegerField(default=0),
        ),
    ]
