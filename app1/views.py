from django.db import connection
from django.shortcuts import render


# Create your views here.
def xyz(request):
    return render(request, "index.html")


def abc(request):
 #   value1 = request.GET['value1']
  #  value2 = request.GET['value2']
   # if "sum" == 'sum':
    #    value3 = value1 + value2
    #else:
     #   value3 = value1-value2
    return render(request, "T1.html")

def signUp(request):
    email = request.GET['email']
    psw = request.GET['psw']

    cursor = connection.cursor()
    query = "insert into users(email,password)values (%s,%s)"
    values = (email,psw)
    cursor.execute(query,values)

    #query = "select customerName from customer where customerNumber = '"+psw+" '"
    #cursor.execute(query)
    #row = cursor.fetchone()
    #print(row)

    data = {"email":email ,"password": psw }
    return render(request, "first.html",data)