from django.http import HttpResponse
from django.shortcuts import render

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
     'cheese_sticks': {
        'сыр, г': 0.3,
        'яйца, шт': 1,
        'мука, г': 0.03,
        'масло, мл': 70,
    },
}

def omlet(request):
    try:
        servings = int(request.GET.get("servings"))
        recipe = {}
        for key,value in DATA['omlet'].items():
            recipe[key] = round(value * servings,2)
    except TypeError:
        recipe = DATA['omlet']    
    context = {
        'recipe': recipe
    }
    return render(request, 'calculator/index.html', context)

def pasta(request):
    try:
        servings = int(request.GET.get("servings"))
        recipe = {}
        for key,value in DATA['pasta'].items():
            recipe[key] = round(value * servings,2)
    except TypeError:
        recipe = DATA['pasta'] 
    context = {
        'recipe': recipe
    }
    return render(request, 'calculator/index.html', context)

def buter(request):
    try:
        servings = int(request.GET.get("servings"))
        recipe = {}
        for key,value in DATA['buter'].items():
            recipe[key] = round(value * servings,2)
    except TypeError:
        recipe = DATA['buter'] 
    context = {
        'recipe': recipe
    }
    return render(request, 'calculator/index.html', context)

def cheese_sticks (request):
    try:
        servings = int(request.GET.get("servings"))
        recipe = {}
        for key,value in DATA['cheese_sticks'].items():
            recipe[key] = round(value * servings,2)
    except TypeError:
        recipe = DATA['cheese_sticks'] 
    context = {
        'recipe': recipe
    }
    return render(request, 'calculator/index.html', context)


