from django.shortcuts import render, reverse
import datetime
import os
from django.http import HttpResponse


DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
}

# Напишите ваш обработчик. Используйте DATA как источник данных
# Результат - render(request, 'calculator/index.html', context)
# В качестве контекста должен быть передан словарь с рецептом:
# context = {
#   'recipe': {
#     'ингредиент1': количество1,
#     'ингредиент2': количество2,
#   }
# }

def recipes_view(request, offset):
    servings = request.GET.get('servings', None)
    text = 'Добавьте в url название рецепта Пример: omlet'
    recipe = None
    if offset:
        if offset in DATA:
            if servings:
                servings = int(servings)
                new_recipe = {}
                for key, value in DATA[offset].items():
                    new_recipe[key] = value * servings
                recipe = new_recipe
            else:
                recipe = DATA[offset]
        else:
            text = 'Такого рецепта не знаю :'
    context = {
        'recipe': recipe,
        'text': text,
    }
    return render(request, 'calculator/index.html', context)


def home_view(request):
    template_name = 'calculator/home.html'
    # впишите правильные адреса страниц, используя
    # функцию `reverse`
    pages = {
        'Главная страница': reverse('home'),
        'Показать текущее время': 'current_time/',
        'Показать содержимое рабочей директории': 'workdir/',
        'Рецепты': 'recipes/',
    }
    context = {
        'pages': pages
    }
    return render(request, template_name, context)


def time_view(request):
    # обратите внимание – здесь HTML шаблона нет, 
    # возвращается просто текст
    current_time = datetime.datetime.now().strftime('%d-%m-%Y %H:%M:%S')
    msg = f'Текущее время: {current_time}'
    return HttpResponse(msg)


def workdir_view(request):
    list_files = '******'.join(os.listdir())
    return HttpResponse(list_files)