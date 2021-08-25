from django.shortcuts import render
from . models import Apps

# Create your views here.
def home_View(request):
    apps_list=Apps.objects.all()
    return render(request,'testapp/home.html',{'apps_list':apps_list})