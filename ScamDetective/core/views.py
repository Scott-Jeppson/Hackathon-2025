from django.shortcuts import render, redirect
from .models import Keyword, CountryCode, Admin, Phrase
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, 'core/index.html')

def input(request):
    return render(request, 'core/Input.html')

def output(request):
    return render(request, 'core/Output.html')

def secretPage(request):
    if request.method == 'GET':
        return render(request, 'core/making_entries.html', {
            'code': CountryCode.objects.order_by('-id').first(),
        })
    elif request.method == 'POST':
        code = request.POST['code']
        country = request.POST['country']
        countryCode = CountryCode.objects.create(country=country, code=code)
        return redirect('/secretPage')