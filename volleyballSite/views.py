from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from .models import User,Match
def index(request):
    return HttpResponse('hello how are u???')

def login(request):
    if 'username' in request.POST:
        try:
            user = User.objects.get(username=request.POST['username'])
            return render(request, 'home.html',{'matches' : Match.objects.all()})

        except:
            return render(request, 'login.html', {'error_message': 'username or password are incorrect'})
    else:
        return render(request,'login.html')
def register(request):
    if 'username' in request.POST:
        try:
            user = User.objects.get(username=request.POST['username'])
            return render(request,'register.html',{'error_message': 'another username registered with given username'})

        except:
            username = request.POST['username']
            password = request.POST['password']
            name = request.POST['name']

            user = User(username = username,name = name ,password = password)
            user.save()
            return render(request,'login.html',{'error_message' : 'you have been registered successfully'})

    return render(request,'register.html')


def buy(request):
    pass
