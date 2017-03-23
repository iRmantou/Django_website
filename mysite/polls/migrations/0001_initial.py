# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GradeOneBanJi',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('BanJi_num1', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='GradeOneChoice',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('choice_text1', models.CharField(max_length=200)),
                ('score1', models.IntegerField(default=0)),
                ('sum1', models.IntegerField(default=0)),
                ('select1', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='GradeOneQuestion',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('question_text1', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='GradeOneSelectt',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('QuestionDescribe1', models.CharField(max_length=200)),
                ('SelectDescribe1', models.CharField(max_length=200)),
                ('Desselect1', models.ForeignKey(to='polls.GradeOneBanJi')),
            ],
        ),
        migrations.CreateModel(
            name='GradeThreeBanJi',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('BanJi_num3', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='GradeThreeChoice',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('choice_text3', models.CharField(max_length=200)),
                ('score3', models.IntegerField(default=0)),
                ('sum3', models.IntegerField(default=0)),
                ('select3', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='GradeThreeQuestion',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('question_text3', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='GradeThreeSelect',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('QuestionDescribe3', models.CharField(max_length=200)),
                ('SelectDescribe3', models.CharField(max_length=200)),
                ('Desselect33', models.ForeignKey(to='polls.GradeThreeBanJi')),
            ],
        ),
        migrations.CreateModel(
            name='GradeTwoBanJi',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('BanJii_num2', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='GradeTwoChoice',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('choice_text2', models.CharField(max_length=200)),
                ('score2', models.IntegerField(default=0)),
                ('sum2', models.IntegerField(default=0)),
                ('select2', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='GradeTwoQuestion',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('question_text2', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='GradeTwoSelect',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('QuestionDescribe2', models.CharField(max_length=200)),
                ('SelectDescribe2', models.CharField(max_length=200)),
                ('Desselect22', models.ForeignKey(to='polls.GradeTwoBanJi')),
            ],
        ),
        migrations.CreateModel(
            name='Studentt',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('student_id', models.CharField(max_length=100)),
                ('class_id', models.CharField(max_length=100)),
                ('grade_id', models.CharField(default='', max_length=100)),
                ('password', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='TeacherChoice',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('choice_text4', models.CharField(max_length=200)),
                ('score4', models.IntegerField(default=0)),
                ('sum4', models.IntegerField(default=0)),
                ('select4', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='TeacherQuestion',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('question_text4', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='teacherchoice',
            name='question4',
            field=models.ForeignKey(to='polls.TeacherQuestion'),
        ),
        migrations.AddField(
            model_name='gradetwochoice',
            name='question2',
            field=models.ForeignKey(to='polls.GradeTwoQuestion'),
        ),
        migrations.AddField(
            model_name='gradethreechoice',
            name='question3',
            field=models.ForeignKey(to='polls.GradeThreeQuestion'),
        ),
        migrations.AddField(
            model_name='gradeonechoice',
            name='question1',
            field=models.ForeignKey(to='polls.GradeOneQuestion'),
        ),
    ]
