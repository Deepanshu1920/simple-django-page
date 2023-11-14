
# from django.shortcuts import get_object_or_404, render
# from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'myapp/home.html')

def details(request):
    key = request.GET.get('key')
    print(key);
    return render(request, 'myapp/details.html', {'name': key})
