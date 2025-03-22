from django.shortcuts import render, redirect
from .models import Keyword, CountryCode, Phrase
from django.http import HttpResponse
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request, 'core/index.html')

def input(request):
    if request.method == 'GET':
        return render(request, 'core/Input.html')
    elif request.method == 'POST':
        currentScore = 0
        currentCode = None

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
                    currentScore += phrase.getScore()
            for keyword in keywords:
                if keyword.compare(message):
                    currentScore += keyword.getScore()
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
                currentCode = parts[0]
                number = parts[1]
            else:
                messages.error(request, 'Invalid phone number format. Please include a space after the country code.')
                return render(request, 'core/Input.html')
            for phrase in phrases:
                if phrase.compare(message):
                    currentScore += phrase.getScore()
            for keyword in keywords:
                if keyword.compare(message):
                    currentScore += keyword.getScore()

        # Store current score and current code in cookies
        response = redirect('/output')
        response.set_cookie('currentScore', currentScore, samesite='Lax')
        response.set_cookie('currentCode', currentCode, samesite='Lax')
        response.set_cookie('currentNumber', number, samesite='Lax')
        response.set_cookie('currentEmail', email, samesite='Lax')
        return response

def output(request):
    # Retrieve current score and current code from cookies
    currentScore = int(request.COOKIES.get('currentScore', 0))
    currentCode = request.COOKIES.get('currentCode', None)
    currentNumber = request.COOKIES.get('currentNumber', None)
    currentEmail = request.COOKIES.get('currentEmail', None)

    phone = False
    source = currentEmail
    if currentNumber:
        phone = True
        c = CountryCode.objects.filter(code=currentCode).first()
        if c:
            source = c.__str__()
        else:
            source = "Unknown Country"
    
    if request.method == 'GET':
        return render(request, 'core/Output.html', {
            'percentage': currentScore,
            'phone': phone,
            'source': source,
        })

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