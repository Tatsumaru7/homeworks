from django.shortcuts import render, redirect
from .models import Phone

def index(request):
    return redirect('catalog')


def show_catalog(request):
    try:
        sort = request.GET.get('sort')
        if sort == 'min_price':
            phones = Phone.objects.order_by('price').all()
        elif sort == 'max_price':
            phones = Phone.objects.order_by('-price').all()
        else:
            phones = Phone.objects.order_by('name').all()
    except Exception:
        phones = Phone.objects.all()
    template = 'catalog.html'
    context = {
        "phones": phones
    }
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    phone = Phone.objects.filter(slug=slug).first()
    context = {
        "phone": phone
    }
    return render(request, template, context)
