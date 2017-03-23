from django.contrib import admin
from polls.models import Studentt
from django import forms
from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect
#  用于操作execl
import xdrlib
import xlrd
# Register your models here.
from .models import GradeOneQuestion, GradeOneChoice, GradeTwoQuestion, GradeTwoChoice
from .models import GradeThreeQuestion, GradeThreeChoice, TeacherQuestion, TeacherChoice

from .models import GradeOneBanJi, GradeOneSelectt
from .models import GradeTwoBanJi, GradeTwoSelect
from .models import GradeThreeBanJi, GradeThreeSelect
from .models import TeacherSelect

from django.contrib import admin
from django.utils.text import capfirst
from django.utils.datastructures import SortedDict


class ChoiceInline1(admin.TabularInline):
    model = GradeOneChoice
    extra = 0
    #fields = ['score1']

class ChoiceInline2(admin.TabularInline):
    model = GradeTwoChoice
    extra = 0

class ChoiceInline3(admin.TabularInline):
    model = GradeThreeChoice
    extra = 0

class ChoiceInline4(admin.TabularInline):
    model = TeacherChoice
    extra = 0

class QuestionOneAdmin(admin.ModelAdmin):  # 创建一个模型管理类，然后将该类（对象）作为第二参数传递给 admin.site.register
    fields = ['question_text1']
    inlines = [ChoiceInline1]


class QuestionTwoAdmin(admin.ModelAdmin):  # 创建一个模型管理类，然后将该类（对象）作为第二参数传递给 admin.site.register
    fields = ['question_text2']
    inlines = [ChoiceInline2]


class QuestionThreeAdmin(admin.ModelAdmin):  # 创建一个模型管理类，然后将该类（对象）作为第二参数传递给 admin.site.register
    fields = ['question_text3']
    inlines = [ChoiceInline3]


class QuestionFourAdmin(admin.ModelAdmin):  # 创建一个模型管理类，然后将该类（对象）作为第二参数传递给 admin.site.register
    fields = ['question_text4']
    inlines = [ChoiceInline4]


class GradeOneSelectAdmin(admin.TabularInline):
    model = GradeOneSelectt
    extra = 0


class OneBanJiAdmin(admin.ModelAdmin):
    fields = ['BanJi_num1']
    inlines = [GradeOneSelectAdmin]


class GradeTwoSelectAdmin(admin.TabularInline):
    model = GradeTwoSelect
    extra = 0


class TwoBanJiAdmin(admin.ModelAdmin):
    fields = ['BanJii_num2']
    inlines = [GradeTwoSelectAdmin]


class GradeThreeSelectAdmin(admin.TabularInline):
    model = GradeThreeSelect
    extra = 0


class ThreeBanJiAdmin(admin.ModelAdmin):
    fields = ['BanJi_num3']
    inlines = [GradeThreeSelectAdmin]


class TeacherSelectAdmin(admin.ModelAdmin):
    list_display = ['QuestionDescribe4', 'SelectDescribe4']


def execl_table_byname(modeladmin, request, queryset):  # 实现了导入学生数据
    file = 'E:\Djangoweb\mysite\student.xlsx'
    by_name = u'Sheet1'
    data = xlrd.open_workbook(file)
    table = data.sheet_by_name(by_name)
    nrows = table.nrows
    ncols = 0  # 学生的学号都放在第一列
    for r in range(0, nrows, +1):
        xuehao = str(int(table.cell_value(r, ncols)))
        pw = xuehao[-4:]  # 后四位作为密码
        Studentt.objects.create(student_id=xuehao, password=pw)  # 将学生的学号输入进去
execl_table_byname.short_description = "添加学生信息"


class StudentAdmin(admin.ModelAdmin):
    list_display = ['student_id', 'class_id', 'password', 'grade_id', 'have_select']
    ordering = ['student_id']
    actions = [execl_table_byname]  # 这里只填写名
    actions_on_top = False
    actions_on_bottom = True
    search_fields = ['student_id']


# 用于控制model顺序
def find_model_index(name):
    count = 0
    for model, model_admin in admin.site._registry.items():
        if capfirst(model._meta.verbose_name_plural) == name:
            return count
        else:
            count += 1
    return count


def index_decorator(func):
    def inner(*args, **kwargs):
        templateresponse = func(*args, **kwargs)
        for app in templateresponse.context_data['app_list']:
            app['models'].sort(key=lambda x: find_model_index(x['name']))
        return templateresponse
    return inner


registry = SortedDict()
registry.update(admin.site._registry)
admin.site._registry = registry
admin.site.index = index_decorator(admin.site.index)
admin.site.app_index = index_decorator(admin.site.app_index)
#admin.site.register(yourmodel, yourmodeladmin)
"""
1、首先使用有序字典替换原来的无序字典作为注册model的数据容器，并把已经存在的数据拷贝到新的有序字典里面。
2、装饰index view 和 app_index view这2个函数，修改templateresponse的返回值里面的context_data，按注册时的顺序重新排序。
3、之后安装正常的django admin register方式使用即可。
4、需要注意的地方，上述代码最好放在比较早运行的地方，比如settings.py 里面自己写的app里面的首个的admin.py文件中
   ，否则在运行到这段代码之前已经注册的admin model是无序的。
"""

# admin.site.register(Media)

admin.site.register(Studentt, StudentAdmin)
admin.site.register(GradeOneQuestion, QuestionOneAdmin)
admin.site.register(GradeTwoQuestion, QuestionTwoAdmin)
admin.site.register(GradeThreeQuestion, QuestionThreeAdmin)
admin.site.register(TeacherQuestion, QuestionFourAdmin)

admin.site.register(GradeOneBanJi, OneBanJiAdmin)
admin.site.register(GradeTwoBanJi, TwoBanJiAdmin)
admin.site.register(GradeThreeBanJi, ThreeBanJiAdmin)
admin.site.register(TeacherSelect, TeacherSelectAdmin)