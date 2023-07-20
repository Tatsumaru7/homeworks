from django.http import HttpResponse
from django.shortcuts import render, reverse
import datetime
import pytz
import os

                      
def home_view(request):
    template_name = 'app/home.html'

    pages = {
        'Главная страница': reverse('home'),
        'Показать текущее время': reverse('time'),
        'Показать содержимое рабочей директории': reverse('workdir')
    }
    
    context = {
        'pages': pages
    }
    return render(request, template_name, context)


def time_view(request):
    # Выбираем Московскую временную зону
    moscow_tz = pytz.timezone('Europe/Moscow')
    return HttpResponse(f'time = {datetime.datetime.now(tz=moscow_tz).time()}')


def workdir_view(request):  
    # Получаем рабочую директорию
    workdir = os.getcwd()
    # Получаем список файлов и каталогов в рабочей директории
    file_list = os.listdir(workdir)
    # Формируем ответ HttpResponse с перечислением файлов
    response_content = "\n".join(file_list)
    return HttpResponse(response_content, content_type='text/plain')
