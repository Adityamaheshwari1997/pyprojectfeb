from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def xyz(request):
    return render(request, "index.html")
def abc(request):
    return HttpResponse("This url is created by a Aditya")
def signUp(request):
    email = request.GET['email']
    psw = request.GET['psw']
    data = {"email":email ,"password": psw }
    return render(request, "first.html",data)