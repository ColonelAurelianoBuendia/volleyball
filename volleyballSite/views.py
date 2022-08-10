from django.shortcuts import render
from django.http import HttpResponse
def index(request):
    return HttpResponse('hello how are u???')

def login(request):
    if 'fname' in request.POST:

        fname = request.POST['fname']
        lname = request.POST['lname']
        return render(request,'login.html',{'fname':fname,'lname':lname})

    return render(request, 'login.html')
