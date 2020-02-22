import os
from datetime import *
from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponse

from . import database
from .models import PageView

# Create your views here.

def index(request):
    hostname = os.getenv('HOSTNAME', 'unknown')
    PageView.objects.create(hostname=hostname)

    return render(request, 'welcome/index.html', {
        'hostname': hostname,
        'database': database.info(),
        'count': PageView.objects.count()
    })

def health(request):
    return HttpResponse(PageView.objects.count())

def hello(request):
    context = {}
    context['hello'] = 'Hello World! Replace Param! '
    context['param1'] = 'Test "hi",\ '' '
    context['pub_date'] = date(2017, 8, 18)
    return render(request, 'hello.html', context)


def showDetail(request):
    return render(request, 'json.txt')
