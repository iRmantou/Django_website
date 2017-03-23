# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_studentt_have_select'),
    ]

    operations = [
        migrations.CreateModel(
            name='TeacherSelect',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('QuestionDescribe4', models.CharField(max_length=200)),
                ('SelectDescribe4', models.CharField(max_length=200)),
            ],
        ),
    ]
