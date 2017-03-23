from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import GradeOneQuestion
from django.template import RequestContext, loader
from django.http import Http404
from django.core.urlresolvers import reverse
from .models import GradeOneChoice, GradeOneQuestion, GradeTwoQuestion, GradeTwoChoice
from .models import GradeThreeQuestion, GradeThreeChoice
from .models import GradeTwoBanJi, GradeThreeBanJi, GradeOneBanJi, Studentt
from .models import GradeOneSelectt, GradeTwoSelect, GradeThreeSelect
from .models import TeacherQuestion, TeacherChoice, TeacherSelect
import os
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.text import capfirst
from django.apps import apps
from django.utils import six
import xlrd, xlwt
import codecs
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django import forms
import copy
import json
from django.contrib.auth import authenticate, login, logout

"""
def index(request):
    latest_question_list = GradeOneQuestion.objects[:2]
    template = loader.get_template('polls/index.html')
    context = RequestContext(request, {
        'latest_question_list': latest_question_list,
    })
    return HttpResponse(template.render(context))
"""


def detail(request):
    latest_question_list = GradeOneQuestion.objects.all()
    return render(request, 'polls/detail.html', {'latest_question_list': latest_question_list})
"""
    try:
        question = GradeOneQuestion.objects.get(pk=question1_id)
    except GradeOneQuestion.DoesNotExist:
        raise Http404("This Question does not exist")  # 如果出现不存在的id，就是说这个问题没有设置，则会引发一个404错误
"""


def vote1(request):
    o = Studentt.objects.filter(student_id=theusername)
    w = Studentt.objects.filter(student_id=theusername).update(have_select=True)
    for a in GradeOneQuestion.objects.all():
        m = get_object_or_404(GradeOneQuestion, pk=a.id)
        s = m.gradeonechoice_set.filter(pk=request.POST[str(a.id)])
        ban = GradeOneBanJi.objects.filter(BanJi_num1=str(o[0].class_id))
        num = 0
        sum = 0
        peo = 0
        z = ban[0].gradeoneselectt_set.filter(QuestionDescribe1=a.question_text1)
        p = str(z[0].SelectDescribe1).split("|")
        for g in m.gradeonechoice_set.all():
            if s[0].choice_text1 == g.choice_text1:
                sum = z[0].sum1 + s[0].score1
                if p[num] == "0":
                    p[num] = "1"
                else:
                    p[num] = str((int(p[num]))+1)
            else:
                num = num+1
        fenge = "|"
        for k in p:
            peo = peo + int(k)
        l = ban[0].gradeoneselectt_set.filter(QuestionDescribe1=a.question_text1).update(SelectDescribe1=fenge.join(p), sum1=sum, average1=sum/peo)
    return HttpResponse("Successful,Thank u")


def vote2(request):
    o = Studentt.objects.filter(student_id=theusername)
    w = Studentt.objects.filter(student_id=theusername).update(have_select=True)
    for a in GradeTwoQuestion.objects.all():
        m = get_object_or_404(GradeTwoQuestion, pk=a.id)
        s = m.gradetwochoice_set.filter(pk=request.POST[str(a.id)])
        ban = GradeTwoBanJi.objects.filter(BanJii_num2=str(o[0].class_id))
        num = 0
        sum = 0
        peo = 0
        z = ban[0].gradetwoselect_set.filter(QuestionDescribe2=a.question_text2)
        p = str(z[0].SelectDescribe2).split("|")
        for g in m.gradetwochoice_set.all():
            if s[0].choice_text2 == g.choice_text2:
                sum = z[0].sum2 + s[0].score2
                if p[num] == "0":
                    p[num] = "1"
                else:
                    p[num] = str((int(p[num]))+1)
            else:
                num = num+1
        fenge = "|"
        for k in p:
            peo = peo + int(k)
        l = ban[0].gradetwoselect_set.filter(QuestionDescribe2=a.question_text2).update(SelectDescribe2=fenge.join(p), sum2=sum, average2=sum/peo)
    return HttpResponse("Successful,Thank u")


def vote3(request):
    o = Studentt.objects.filter(student_id=theusername)
    w = Studentt.objects.filter(student_id=theusername).update(have_select=True)
    for a in GradeThreeQuestion.objects.all():
        m = get_object_or_404(GradeThreeQuestion, pk=a.id)
        s = m.gradethreechoice_set.filter(pk=request.POST[str(a.id)])
        ban = GradeThreeBanJi.objects.filter(BanJi_num3=str(o[0].class_id))
        num = 0
        sum = 0
        peo = 0
        z = ban[0].gradethreeselect_set.filter(QuestionDescribe3=a.question_text3)
        p = str(z[0].SelectDescribe3).split("|")
        for g in m.gradethreechoice_set.all():
            if s[0].choice_text3 == g.choice_text3:
                sum = z[0].sum3 + s[0].score3
                if p[num] == "0":
                    p[num] = "1"
                else:
                    p[num] = str((int(p[num]))+1)
            else:
                num = num+1
        fenge = "|"
        for k in p:
            peo = peo + int(k)
        l = ban[0].gradethreeselect_set.filter(QuestionDescribe3=a.question_text3).update(SelectDescribe3=fenge.join(p), sum3=sum, average3=sum/peo)
    return HttpResponse("Successful,Thank u")


# 老师的身份信息也存储在 学生表中
def vote4(request):
    o = Studentt.objects.filter(student_id=theusername)
    w = Studentt.objects.filter(student_id=theusername).update(have_select=True)
    for a in TeacherQuestion.objects.all():
        m = get_object_or_404(TeacherQuestion, pk=a.id)
        s = m.teacherchoice_set.filter(pk=request.POST[str(a.id)])
        num = 0
        sum = 0
        peo = 0
        z = TeacherSelect.objects.filter(QuestionDescribe4=a.question_text4)
        p = str(z[0].SelectDescribe4).split("|")
        for g in m.teacherchoice_set.all():
            if s[0].choice_text4 == g.choice_text4:
                sum = z[0].sum4 + s[0].score4
                if p[num] == "0":
                    p[num] = "1"
                else:
                    p[num] = str((int(p[num]))+1)
            else:
                num = num+1
        fenge = "|"
        for k in p:
            peo = peo + int(k)
        l = TeacherSelect.objects.filter(QuestionDescribe4=a.question_text4).update(SelectDescribe4=fenge.join(p), sum4=sum, average4=sum/peo)
    return HttpResponse("Successful,Thank u")
"""
    p = get_object_or_404(GradeOneQuestion, pk=question_id)
    selected_choice = p.gradeonechoice_set.get(pk=request.POST[question_id])
    selected_choice.votes1 += 1
    selected_choice.save()
    return HttpResponseRedirect(reverse('polls:results', args=(p.id,)))
"""


def results(request, question1_id):
    question = get_object_or_404(GradeOneQuestion, pk=question1_id)
    return render(request, 'polls/results.html', {'question': question})


# 视图函数可以输出xml，pdf等
# 具体分段上传过程
def handle_uploaded_file(file, filename):
    if not os.path.exists('upload/'):
        os.mkdir('upload/')
    with open('upload/' + filename, 'wb+') as destination:
        for chunk in file.chunks():
            destination.write(chunk)


# admin上传学生信息名单文件 模型，包括execl操作
def upload(request):
    if request.method == 'POST':
        handle_uploaded_file(request.FILES['file'], str(request.FILES['file']))
        file = 'E:\\Djangoweb\\mysite\\upload\\' + str(request.FILES['file'])  # 原来这里出了一些问题，必须要\\进行转义
        by_name = u'Sheet1'
        data = xlrd.open_workbook(file)
        table = data.sheet_by_name(by_name)
        nrows = table.nrows
        ncols = 0  # 学生的学号都放在第一列
        for r in range(0, nrows, +1):
            xuehao = str(table.cell_value(r, ncols))   ###qaudiao int
            pw = xuehao[-4:]  # 后四位作为密码
            Studentt.objects.create(student_id=xuehao, password=pw)  # 将学生的学号输入进去
        return HttpResponse("Successful")  # 相同的文件会自动覆盖不提醒
    return HttpResponse("Failed")


def getResult(request):
    if request.method == 'POST':
        file = xlwt.Workbook()
        table = file.add_sheet('result')

        num = 1
        name = ''
        table.write(0, 0, "年级")
        table.write(0, 1, "班级")
        for q1 in range(max(len(GradeOneQuestion.objects.all()),len(GradeTwoQuestion.objects.all()),len((GradeThreeQuestion.objects.all())))):
            name = "第"+str(num)+"题"
            table.write(0, num+1, name)
            num = num + 1


        nrow = 1 # 行
        ncol = 0 # 列
        for ban1 in GradeOneBanJi.objects.all():
            table.write(nrow, ncol, "高一")
            ncol = ncol+1
            table.write(nrow, ncol, ban1.BanJi_num1)
            ncol = ncol + 1
            for r1 in ban1.gradeoneselectt_set.all():
                table.write(nrow, ncol, r1.average1)
                ncol = ncol + 1
            nrow =nrow+1
            ncol = 0

        for ban2 in GradeTwoBanJi.objects.all():
            table.write(nrow, ncol, "高二")
            ncol = ncol + 1
            table.write(nrow, ncol, ban2.BanJii_num2)
            ncol = ncol + 1
            for r2 in ban2.gradetwoselect_set.all():
                table.write(nrow, ncol, r2.average2)
                ncol = ncol + 1
            nrow = nrow + 1
            ncol = 0

        for ban3 in GradeThreeBanJi.objects.all():
            table.write(nrow, ncol, "高三")
            ncol = ncol + 1
            table.write(nrow, ncol, ban3.BanJi_num3)
            ncol = ncol + 1
            for r3 in ban3.gradethreeselect_set.all():
                table.write(nrow, ncol, r3.average3)
                ncol = ncol + 1
            nrow = nrow + 1
            ncol = 0

        table.write(nrow, ncol, "教师")
        ncol = ncol+1
        table.write(nrow, ncol, "无")
        ncol = ncol+1
        for thacher in TeacherSelect.objects.all():
            table.write(nrow, ncol, thacher.average4)
            ncol = ncol+1

        file.save('C:\\Users\\Administrator\\Desktop\\result.xlsx')
        #file.save('E:\\Djangoweb\\mysite\\upload\\result.xlsx')
        return HttpResponse("Successful")
    return HttpResponse("Failed")

# 更细各个班级中的问题表述，并且把统计结果清零！！！
def questionclassdata(request):
    if request.method == 'POST':
        for onebanji in GradeOneBanJi.objects.all():
            for one in onebanji.gradeoneselectt_set.all():
                one.delete()
            for onebanjiselect in GradeOneQuestion.objects.all():
                a1 = "0|"
                x1 = 0
                for i in range(len(onebanjiselect.gradeonechoice_set.all())):
                    if x1+2 == len(onebanjiselect.gradeonechoice_set.all()):
                        a1 = a1 + "0"
                        break
                    else:
                        x1 = x1+1
                        a1 = a1+"0|"
                GradeOneSelectt.objects.create(Desselect1=onebanji, QuestionDescribe1=onebanjiselect.question_text1, SelectDescribe1=a1)


        for twobanji in GradeTwoBanJi.objects.all():
            for two in twobanji.gradetwoselect_set.all():
                two.delete()
            for twobanjiselect in GradeTwoQuestion.objects.all():
                a2 = "0|"
                x2 = 0
                for i in range(len(twobanjiselect.gradetwochoice_set.all())):
                    if x2 + 2 == len(twobanjiselect.gradetwochoice_set.all()):
                        a2 = a2 + "0"
                        break
                    else:
                        x2 = x2 + 1
                        a2 = a2 + "0|"
                GradeTwoSelect.objects.create(Desselect22=twobanji, QuestionDescribe2=twobanjiselect.question_text2, SelectDescribe2=a2)


        for threebanji in GradeThreeBanJi.objects.all():
            for three in threebanji.gradethreeselect_set.all():
                three.delete()
            for threebanjiselect in GradeThreeQuestion.objects.all():
                a3 = "0|"
                x3 = 0
                for i in range(len(threebanjiselect.gradethreechoice_set.all())):
                    if x3 + 2 == len(threebanjiselect.gradethreechoice_set.all()):
                        a3 = a3 + "0"
                        break
                    else:
                        x3 = x3 + 1
                        a3 = a3 + "0|"
                GradeThreeSelect.objects.create(Desselect33=threebanji, QuestionDescribe3=threebanjiselect.question_text3, SelectDescribe3=a3)


        for teacherss in TeacherSelect.objects.all():
            teacherss.delete()
        for teacher in TeacherQuestion.objects.all():
            a4 = "0|"
            x4 = 0
            for i in range(len(teacher.teacherchoice_set.all())):
                if x4 + 2 == len(teacher.teacherchoice_set.all()):
                    a4 = a4 + "0"
                    break
                else:
                    x4 = x4 + 1
                    a4 = a4 + "0|"
            TeacherSelect.objects.create(QuestionDescribe4=teacher.question_text4,
                                            SelectDescribe4=a4)


        return HttpResponse("Successful")
    return HttpResponse("Failed")


# 定义表单模型
class UserForm(forms.Form):
    username = forms.CharField(label='用户名', max_length=100, )
    password = forms.CharField(label="密  码", widget=forms.PasswordInput())


theusername = "" #全局变量


# 登录控制
def login(request):
    if request.method == 'POST':
        g = request.POST['grade']
        c = request.POST['classnum']
        if g == "Your Grade" or c == "Your Class":
            response = HttpResponse()
            response.write('<script>alert("请选择年级与班级");history.go(-1);</script>')  # 学生不填写年级会返回原来界面
            return response
            #return HttpResponseRedirect('http://127.0.0.1:8000/polls/Login/')
        uf = UserForm(request.POST)
        if uf.is_valid():
            # 获取表单用户密码
            username = uf.cleaned_data['username']
            password = uf.cleaned_data['password']
            # 获取的表单数据与数据库进行比较
            userr = Studentt.objects.filter(student_id__exact=username, password__exact=password)
            if userr and userr[0].have_select is False:
                global theusername # 相当于全局变量
                theusername = userr[0].student_id
                userr[0].SetClass(str(c))
                userr[0].SetGrade(str(g))
                userr[0].save()  # !!!!!需要save才能保存数据
                if userr[0].student_id[0] == 'T':
                    latest_question_list = TeacherQuestion.objects.all()
                    return render(request, 'polls/Q_FOUR.html', {'latest_question_list': latest_question_list})
                elif str(g) == "Grade1":
                    latest_question_list = GradeOneQuestion.objects.all()
                    return render(request, 'polls/Q_ONE.html', {'latest_question_list': latest_question_list})
                elif str(g) == "Grade2":
                    latest_question_list = GradeTwoQuestion.objects.all()
                    return render(request, 'polls/Q_TWO.html', {'latest_question_list': latest_question_list})
                elif str(g) == "Grade3":
                    latest_question_list = GradeThreeQuestion.objects.all()
                    return render(request, 'polls/Q_THREE.html', {'latest_question_list': latest_question_list})

                #return render(request, 'polls/QUESTIONS.html', {'latest_question_list': latest_question_list, "mm":mm})
                    #return render_to_response('polls/success.html', {'username': username}, context_instance=RequestContext(request))
            else:
                return HttpResponseRedirect('http://127.0.0.1:8000')  # 如果验证错误，则返回登陆界面
    else:
        uf = UserForm()
    return render_to_response('polls/login.html', {'uf': uf}, context_instance=RequestContext(request))


# 多级联动下拉列表获取班级
def Return_Class_Data(request):
    province = request.GET['Gradenum']
    print(province)
    City_list = []
    if province == "Grade1":
        for city in GradeOneBanJi.objects.all():
            City_list.append(city.BanJi_num1)
    elif province == "Grade2":
        for city in GradeTwoBanJi.objects.all():
            City_list.append(city.BanJii_num2)
    elif province == "Grade3":
        for city in GradeThreeBanJi.objects.all():
            City_list.append(city.BanJi_num3)
    return HttpResponse(json.dumps(City_list))
