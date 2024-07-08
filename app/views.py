import datetime
import os
from typing import re

from django.http import HttpResponse
from django.shortcuts import render, reverse


def home_view(request):
    template_name = 'app/home.html'
    # впишите правильные адреса страниц, используя
    # функцию `reverse`
    pages = {
        'Главная страница': reverse('home'),
        'Показать текущее время': reverse('time'),
        'Показать содержимое рабочей директории': reverse('workdir')
    }

    # context и параметры render менять не нужно
    # подбробнее о них мы поговорим на следующих лекциях
    context = {
        'pages': pages
    }
    return render(request, template_name, context)


def time_view(request):
    template_name = 'app/time.html'

    # обратите внимание – здесь HTML шаблона нет, 
    # возвращается просто текст
    current_time = datetime.datetime.now().time().strftime('%H:%M:%S')
    msg = f'Текущее время: {current_time}'
    # return HttpResponse(msg)
    return render(request, template_name, context={'time_c': current_time})


def workdir_view(request):
    # по аналогии с `time_view`, напишите код,
    # который возвращает список файлов в рабочей
    # директории
    list_dir = os.listdir('.')
    template_name = 'app/list_directory.html'
    # return HttpResponse('</br>'.join(li))
    return render(request, template_name, context={'list_dir': list_dir})
