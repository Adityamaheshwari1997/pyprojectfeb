from django.db import connection
from django.shortcuts import render
import random


# Create your views here.
def xyz(request):
    return render(request, "index.html")
def signIn(request):
    return render(request, "index2.html")




def signUp(request):
    email = request.POST['email']
    psw = request.POST['psw']
    mobile = request.POST['Mobile_name']
    gender = request.POST['gender']

    cursor = connection.cursor()
    query1 = "select * from users where email =  '" + email + " ' "
    cursor.execute(query1)
    data = cursor.fetchall()
    if len(data)>0:
        data = {"email": "Already signup...."}
        return render(request,"index2.html",data)
    else:
        otp = random.randint(1000, 9999)
        strotp = str(otp)
        query = "insert into users(email,psw,mobile,gender,otp)values(%s,%s,%s,%s,%s)"
        values = (email,psw,mobile,gender,strotp)
        cursor.execute(query,values)
        data = {"email": email, "password": psw, "mobile": mobile, "gender": gender}
        return render(request, "signupsuccess.html", data)

    #query = "select customerName from customer where customerNumber = '"+psw+" '"
    #cursor.execute(query)
    #row = cursor.fetchone()
    #print(row)

def logIn(request):
    email = request.GET['uname']
    psw = request.GET['psw']

    cursor =connection.cursor()
    query = "select * from users where email = '"+email+" '"
    cursor.execute(query)
    row = cursor.fetchone()
    if row is None:
        data = {"email": "Signin First...."}
        return render(request, "index.html", data)
    else:
        if row[2] == psw:
            data = {"email": email, "password": psw}
            return render(request, "T1.html", data)
        else:
            data = {"email": "password is incorrect"}
            return render(request, "T1.html", data)

def otpVerification(request):
    email = request.GET['email']
    otp = request.GET['otp']

    cursor = connection.cursor()
    query = "select * from users where email = '"+email+" '"
    cursor.execute(query)
    row = cursor.fetchone()

    if row is not None:
        if row[5] == otp:
            query1 = "update users set is_verify = True where email = '"+email+" '"
            cursor.execute(query1)
            if cursor.rowcount == 1:
                print("OTP verified Successfully")
                data = {"email": "OTP verified Successfully"}
                return render(request, "T1.html", data)
        else:
            data = {"email": "please enter correct OTP"}
            return render(request, "T1.html", data)


