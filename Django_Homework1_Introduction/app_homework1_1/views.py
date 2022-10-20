from django.http import HttpResponse
from datetime import datetime
import os
from django.shortcuts import render, reverse

# Create your views here.
def homepage(request):
    template_name = 'app_homework1_1/home.html'
    # впишите правильные адреса страниц, используя функцию `reverse`
    pages = {
        'Главная страница': reverse('homepage'),
        'Показать текущее время': reverse('current_time'),
        'Показать содержимое рабочей директории': reverse('workdir')
    }
    # context и параметры render менять не нужно
    context = {
        'pages': pages
    }

    return render(request, template_name, context)
    #return HttpResponse("<h4>Список доступных страниц</4>")


def current_time(request):
    horologe = f"Текущее время: {datetime.now().time()} <br><a href='{reverse('homepage')}'>На главную</a>"

    return HttpResponse(horologe)


def workdir(request):
    path = "/home/ideapad5/Нетология. Python-разработчик с нуля. PD-58/Django/1. Знакомство с Django. Подготовка и запуск проекта./Django_Homework1_Introduction"
    filelist = []
    for root, dirs, files in os.walk(path):
        for file in files:
            filelist.append(os.path.join(root, file))
    all_dir_files = f"Содержимое рабочей директории: {filelist} <br><a href='{reverse('homepage')}'>На главную</a>"

    return HttpResponse(all_dir_files)
