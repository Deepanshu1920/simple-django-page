
# from django.shortcuts import get_object_or_404, render
# from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse

# from django.template import loader
# from models import Member
# def detail_user(request):
#     return render(request, 'myapp/templates/myapp/all_members.html')
def home(request):
    return render(request, 'myapp/home.html')

def details(request):
    key = request.GET.get('key')
    print(key);
    return render(request, 'myapp/details.html', {'name': key})
# def details(request):    
#     return HttpResponse('<h1>This is about me!.</h1>') 
# def detail_user(request):
#   return HttpResponse("detail about user")
#
# def members(request):
#   mymembers = Member.objects.all().values()
#   template = loader.get_template('all_members.html')
#   context = {
#     'mymembers': mymembers,
#   }
#   return HttpResponse(template.render(context, request))
#
# def details(request, id):
#   mymember = Member.objects.get(id=id)
#   template = loader.get_template('details.html')
#   context = {
#     'mymember': mymember,
#   }
#   return HttpResponse(template.render(context, request))
#
#   def render_items(request, item_name):
#     item = get_object_or_404(YOUR_MODEL, YOUR_ITEM_FIELD_NAME=item_name)
#     return render(request, 'home.html', {'item': item})

