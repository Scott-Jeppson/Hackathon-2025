from django.shortcuts import render, redirect
from .models import Keyword, CountryCode, Phrase
from django.http import HttpResponse
from django.contrib import messages

CURRENT_SCORE = 0
CURRENT_CODE = None

# Create your views here.
def home(request):
    return render(request, 'core/index.html')

def input(request):
    if request.method == 'GET':
        return render(request, 'core/Input.html')
    elif request.method == 'POST':
        CURRENT_SCORE = 0
        # Get the data from the form
        email = request.POST['email']
        number = request.POST['phoneNumber']
        state = request.POST['state']
        message = request.POST['message']

        # Get keywords and phrases from the database
        keywords = Keyword.objects.all()
        phrases = Phrase.objects.all()

        # Figure out if this is an email or a text message
        if '@' in email:
            for phrase in phrases:
                if phrase.compare(message):
                    CURRENT_SCORE += phrase.getScore()
            for keyword in keywords:
                if keyword.compare(message):
                    CURRENT_SCORE += keyword.getScore()
            return redirect('/output')
        else:
            if not number:
                messages.error(request, 'Please enter a phone number or an email address')
                return render(request, 'core/Input.html')
            if not number.startswith('+'):
                messages.error(request, 'Please include the country code of the phone number. It is found at the beginning of the number.')
                return render(request, 'core/Input.html')
            # Strip '+' and split the number
            number = number.lstrip('+')
            parts = number.split(' ', 1)
            if len(parts) == 2:
                CURRENT_CODE = parts[0]
                number = parts[1]
            else:
                messages.error(request, 'Invalid phone number format. Please include a space after the country code.')
                return render(request, 'core/index.html')
            for phrase in phrases:
                if phrase.compare(message):
                    CURRENT_SCORE += phrase.getScore()
            for keyword in keywords:
                if keyword.compare(message):
                    CURRENT_SCORE += keyword.getScore()
            return redirect('/output')

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