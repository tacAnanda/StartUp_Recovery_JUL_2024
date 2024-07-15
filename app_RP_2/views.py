from django.shortcuts import render

from app_RP_2.models import USER_INFO

# Create your views here.


def home(request):
    userinfo = USER_INFO.objects.all()
    context={
        'userinfo':userinfo
            }   
    return render (request, 'index.html', context)



def project_work(request):
    return render (request,'projects.html')


def resume(request):
    return render(request,'resume.html')



def contact(request):
    return render(request, "contact.html")

