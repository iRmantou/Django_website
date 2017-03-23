import datetime
from datetime import datetime, timedelta

#from __future__ import division
import os
from django.db import models
from django.utils import timezone
#from mysite.settings import MEDIA_ROOT
from django.db.models.fields.files import File
from django.db.models.fields.files import FieldFile
from django.utils.translation import ugettext as _
# Create your models here.


UPLOAD_ROOT = 'upload'
"""
class Question(models.Model):
    def __init__(self):
        question_text = models.CharField(max_length=200)
        pub_date = models.DateTimeField('date published')

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

    def __str__(self):
        return self.question_text

"""


class GradeOneQuestion(models.Model):
    question_text1 = models.CharField(max_length=200)  # 问题描述字段

    def __str__(self):
        return self.question_text1


class GradeTwoQuestion(models.Model):
    question_text2 = models.CharField(max_length=200)

    def __str__(self):
        return self.question_text2


class GradeThreeQuestion(models.Model):
    question_text3 = models.CharField(max_length=200)

    def __str__(self):
        return self.question_text3


#  老师的问题表
class TeacherQuestion(models.Model):
    question_text4 = models.CharField(max_length=200)

    def __str__(self):
        return self.question_text4

"""
class Choice(models.Model):
    question = models.ForeignKey(GradeOne_Question)  #每个choice只关联一个question，外码
    def __init__(self):
        self.choice_text = models.CharField(max_length=200)
        self.votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
"""


class GradeOneChoice(models.Model):
    question1 = models.ForeignKey(GradeOneQuestion)  # 每个choice只关联一个question，外码,question1是参照GradeOneQuestion主码的外码
    choice_text1 = models.CharField(max_length=200)  # 选项描述字段
    score1 = models.IntegerField(default=0)  # 用于设置该问题的默认分数
    #sum1 = models.IntegerField(default=0)    # 用于统计整个年级选择该选项的总  人数  ！
    select1 = models.BooleanField(default=False)    # 用于判断这个选项是否被选择 !!!! 需要输入默认类型

    def __str__(self):
        return self.choice_text1


class GradeTwoChoice(models.Model):
    question2 = models.ForeignKey(GradeTwoQuestion)
    choice_text2 = models.CharField(max_length=200)
    score2 = models.IntegerField(default=0)
    #sum2 = models.IntegerField(default=0)
    select2 = models.BooleanField(default=False)

    def __str__(self):
        return self.choice_text2


class GradeThreeChoice(models.Model):
    question3 = models.ForeignKey(GradeThreeQuestion)
    choice_text3 = models.CharField(max_length=200)
    score3 = models.IntegerField(default=0)
    #sum3 = models.IntegerField(default=0)
    select3 = models.BooleanField(default=False)

    def __str__(self):
        return self.choice_text3


#  老师的选项表
class TeacherChoice(models.Model):
    question4 = models.ForeignKey(TeacherQuestion)
    choice_text4 = models.CharField(max_length=200)
    score4 = models.IntegerField(default=0)
    #sum4 = models.IntegerField(default=0)
    select4 = models.BooleanField(default=False)

    def __str__(self):
        return self.choice_text4


#  建立高一学生表,用于登陆系统，号码字段对应并且输入了班级，才能进行相应的选择
class Studentt(models.Model):
    student_id = models.CharField(max_length=100)  # 这个字段用于填写学号/考籍号
    class_id = models.CharField(max_length=100)    # 用于存储学生的班级
    grade_id = models.CharField(max_length=100, default='')
    password = models.CharField(max_length=100)    # 每个学生拥有一个密码
    have_select = models.BooleanField(default=False)

    def SetClass(self,classnum):
        self.class_id = classnum

    def SetGrade(self,gradenum):
        self.grade_id = gradenum


"""
class Media(models.Model):
    filename = models.FileField(upload_to=UPLOAD_ROOT, blank=True)  # 上传文件的路径

    def save(self):
        filename = FieldFile.open(os.path.join(MEDIA_ROOT, self.filename.name))
        filename.save(os.path.join(MEDIA_ROOT, self.filename.name))
        super(Media, self).save()
"""


#  高一班级表，用于统计每个班级关于每一个问题每一个选项的选择情况选择情况
class GradeOneBanJi(models.Model):
    BanJi_num1 = models.CharField(max_length=100)

    def __str__(self):
        return self.BanJi_num1


class GradeOneSelectt(models.Model):
    Desselect1 = models.ForeignKey(GradeOneBanJi)
    QuestionDescribe1 = models.CharField(max_length=200)
    SelectDescribe1 = models.CharField(max_length=200)
    average1 = models.IntegerField(default=0)
    sum1 = models.IntegerField(default=0)


#  高二班级表
class GradeTwoBanJi(models.Model):
    BanJii_num2 = models.CharField(max_length=100)

    def __str__(self):
        return self.BanJii_num2


class GradeTwoSelect(models.Model):
    Desselect22 = models.ForeignKey(GradeTwoBanJi)
    QuestionDescribe2 = models.CharField(max_length=200)
    SelectDescribe2 = models.CharField(max_length=200)
    average2 = models.IntegerField(default=0)
    sum2 = models.IntegerField(default=0)


#  高三班级表
class GradeThreeBanJi(models.Model):
    BanJi_num3 = models.CharField(max_length=100)

    def __str__(self):
        return self.BanJi_num3


class GradeThreeSelect(models.Model):
    Desselect33 = models.ForeignKey(GradeThreeBanJi)
    QuestionDescribe3 = models.CharField(max_length=200)
    SelectDescribe3 = models.CharField(max_length=200)
    average3 = models.IntegerField(default=0)
    sum3 = models.IntegerField(default=0)

class TeacherSelect(models.Model):
    QuestionDescribe4 = models.CharField(max_length=200)
    SelectDescribe4 = models.CharField(max_length=200)
    average4 = models.IntegerField(default=0)
    sum4 = models.IntegerField(default=0)