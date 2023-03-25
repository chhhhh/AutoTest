from django.http import HttpRequest, HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from .models import Subject, Teacher, User
from .serializers import SubjectSerializer
from .utils.captcha import gen_random_code, Captcha
from .utils.md5 import gen_md5_digest
from rest_framework import serializers


# Create your views here.
@api_view(('GET', ))
def show_subjects(request: HttpRequest) -> HttpResponse:
    subjects = Subject.objects.all().order_by('no')
    serializer = SubjectSerializer(subjects, many=True)
    return Response(serializer.data)


class SubjectView(ListAPIView):
    # 通过queryset指定如何获取学科数据
    queryset = Subject.objects.all()
    # 通过serializer_class指定如何序列化学科数据
    serializer_class = SubjectSerializer


def index(request: HttpRequest) -> HttpResponse:
    return render()


def show_teachers(request):
    try:
        sno = int(request.GET.get('sno'))
        teachers = []
        if sno:
            subject = Subject.objects.only('name').get(no=sno)
            teachers = Teacher.objects.filter(subject=subject).order_by('no')
            return render(request, '../static/html/teachers.html', {
                'subject': subject,
                'teachers': teachers
            })
    except (ValueError, Subject.DoesNotExist):
        return redirect('/')


def praise_or_criticize(request):
    if request.session.get('userid'):
        try:
            tno = int(request.GET.get('tno'))
            teacher = Teacher.objects.get(no=tno)
            if request.path.startswith('/praise/'):
                teacher.good_count += 1
                count = teacher.good_count
            else:
                teacher.bad_count += 1
                count = teacher.bad_count
            teacher.save()
            data = {'code': 20000, 'mes': '操作成功', 'count': count}
        except (ValueError, Teacher.DoesNotExist):
            data = {'code': 20001, 'mes': '操作失败'}
    else:
        data = {'code': 20002, 'mes': '请先登录'}
        return JsonResponse(data)


def get_captcha(request: HttpRequest) -> HttpResponse:
    """验证码"""
    captcha_text = gen_random_code()
    request.session['captcha'] = captcha_text
    image_data = Captcha.instance().generate(captcha_text)
    return HttpResponse(image_data, content_type='image/png')


def login(request: HttpRequest) -> HttpResponse:
    hint = ''
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if username and password:
            password = gen_md5_digest(password)
            user = User.objects.filter(username=username, password=password).first()
            if user:
                request.session['userid'] = user.no
                request.session['username'] = user.username
                return redirect('/')
            else:
                hint = '用户名或密码错误'
        else:
            hint = '请输入有效的用户名和密码'
    return render(request, '../static/html/login.html', {'hint': hint})


def logout(request):
    """注销"""
    request.session.flush()
    return redirect('/')
