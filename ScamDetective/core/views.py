from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'core/index.html')

def input(request):
    return render(request, 'core/Input.html')

def output(request):
    return render(request, 'core/Output.html')
