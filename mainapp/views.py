from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import KlientForm
from .models import Produkt


def home(request):
    obj = Produkt.objects.filter(isRecommended=True, dostepnosc='dostępny')
    context = {
        'obj': obj
    }

    return render(request, 'home.html', context)


def login_page(request):
    login = request.POST['uname']
    password = request.POST['psw']
    #   sprawdzenie czy taki login i haslo sa w bazie danych

    return render(request, 'login_page.html', {'login': login, 'password': password})


def register_page(request):
    # return render(request, 'register_page.html')
    if request.method == 'POST':
        form = KlientForm(request.POST)
        if form.is_valid():
            form.save()
            # form = KlientForm()

    else:
        form = KlientForm()
    return render(request, 'register_page.html', {'form': form})


def register_complete(request):
    return render(request, 'register_complete.html')


def cds(request):
    cd = Produkt.objects.filter(dostepnosc='dostępny')

    context = {
        'cd': cd,
    }
    return render(request, 'cds.html', context)


def rock(request):
    cd = Produkt.objects.filter(gatunek='Rock', dostepnosc='dostępny')

    context = {
        'cd': cd,
    }
    return render(request, 'rock.html', context)


def pop(request):
    cd = Produkt.objects.filter(gatunek='POP', dostepnosc='dostępny')
    context = {
        'cd': cd,
    }
    return render(request, 'pop.html', context)
