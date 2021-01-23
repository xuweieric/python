from django.http import HttpResponse
from django.shortcuts import render
from django.template import Template
from django.template.context import Context

from app01.models import *


# Create your views here.

def runoob(request):
    views_dict = {"name": "菜鸟教程", "age": 18}
    return render(request, "runoob.html", {"views_dict": views_dict})


def index(request):
    return renderResponse(request);
    return renderResponse(request)


# render输出
def renderResponse(request):
    return render(request, "index.html", {"categoryList": Category.objects.all()})


# 原始输出的
def templateResponse():
    import os
    print(__file__)
    print(os.path.dirname(__file__))
    base_dir = os.path.dirname(os.path.dirname(__file__))
    with open(os.path.join(base_dir, "templates/index.html")) as fr:
        content = fr.read()
    t = Template(content)
    c = Context({"categoryList": Category.objects.all()})
    respHtml = t.render(c)
    return HttpResponse(respHtml)
