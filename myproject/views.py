# from django.http import HttpResponse
from django.shortcuts import render
#
# def detail_user(request):
#     return HttpResponse("detail about user")
def details(request):
    return render(request, 'myapp/details.html')
