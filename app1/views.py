import string

from django.db import connection
from django.shortcuts import render
from django.core.mail import send_mail
from django.shortcuts import redirect
from django.http import JsonResponse
import random



# Create your views here.
def xyz(request):
<<<<<<< HEAD
    return render(request, "home.html")
def signIn(request):
    return render(request, "index2.html")




=======
    return render(request, "index.html")
def signIn(request):
    return render(request, "index2.html")

>>>>>>> 0f5a11c (new pc git try)
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


        body = 'your otp for our portal you signed up with this email '+ email + ' is ' +strotp
        send_mail('OTP for verification',body,'adityamaheshwari146@gmail.com',[email])


        data = {"email": email, "password": psw, "mobile": mobile, "gender": gender}
        return render(request, "signupsuccess.html", data)

    #query = "select customerName from customer where customerNumber = '"+psw+" '"
    #cursor.execute(query)
    #row = cursor.fetchone()
    #print(row)

def logIn(request):
    email = request.POST['uname']
    psw = request.POST['psw']

    cursor =connection.cursor()

    # query = "select * from users where email = '"+email+" '"
    # cursor.execute(query)

    values = [email]
    res = cursor.callproc('signin',values)
    row = cursor.fetchone()
    if row is None:
        data = {"email": "Signin First...."}
        return render(request, "index.html", data)
    else:
        if row[2] == psw:
            cursor = connection.cursor()
            query = "select * from links where created_by = '" + email + " '"
            cursor.execute(query)
            row = cursor.fetchall()
            row = {"row":row}
            return render(request, "Afterlogin.html", row)
        else:
            data = {"email": "password is incorrect"}
            return render(request, "T1.html", data)

def otpVerification(request):
    email = request.GET['email']
    otp = request.GET['otp']

    cursor = connection.cursor()
    # query = "select * from users where email = '"+email+" '"
    # cursor.execute(query)
<<<<<<< HEAD
    
=======

>>>>>>> 0f5a11c (new pc git try)
    values = [email]
    res = cursor.callproc('signin', values)
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

def urlshortner(request):
    longlink = request.GET['link']
    customurl = request.GET['customurl']

    if customurl is None or customurl == '':
       shortURL = generateShortURL()
    else:
        cursor = connection.cursor()
        query = "select * from links where short_link = '" + customurl + " '"
        cursor.execute(query)
        row = cursor.fetchone()


        if row is not None:
            data = {"email": "This custom URL Already exist please try another one "}
            return render(request, "T1.html", data)
        else:
            query = "insert into links(long_link,short_link)values(%s,%s)"
            values = (longlink, customurl)
            cursor.execute(query, values)

            data = {"email": "your URL is shorting with Adi.cc/"+customurl}
            return render(request, "T1.html", data)

    if shortURL is not None or shortURL != '':
        cursor = connection.cursor()
        query = "select * from links where short_link = '" + shortURL + " '"
        cursor.execute(query)
        row = cursor.fetchone()

        if row is not None:
            data = {"email": "This custom URL Already exist please try another one "}
            return render(request, "T1.html", data)
        else:
            query = "insert into links(long_link,short_link)values(%s,%s)"
            values = (longlink, shortURL)
            cursor.execute(query, values)

            data = {"email": "your URL is shorting with name.co/"+shortURL}
            return render(request, "T1.html", data)

def generateShortURL():
    letters = string.ascii_letters + string.digits
    shortURL = ''

    for i in range(6):
<<<<<<< HEAD
        shortURL =shortURL+ ''.join(random.choice(letters))
=======
        shortURL = shortURL+ ''.join(random.choice(letters))
>>>>>>> 0f5a11c (new pc git try)
    return shortURL

def forgetPsw(request):
    return render(request)

<<<<<<< HEAD

=======
>>>>>>> 0f5a11c (new pc git try)
def handlingShortUrl(request, **kwargs):
    url = kwargs.get('url')
    cursor = connection.cursor()
    query = "select long_link from links where short_link = '" + url + " '"
    cursor.execute(query)
    row = cursor.fetchone()
    if row is None:
        return render(request, "home.html")
    else:
        return redirect(row[0])

def edit(request):
    value = request.GET['id']

    cursor = connection.cursor()
    query = "select * from links where id = '" + value + " '"
    cursor.execute(query)
    row = cursor.fetchone()

    data = {"data": row}
    return render(request, "Editoption.html", data)

def generateShortURLApi(request):
    letters = string.ascii_letters + string.digits
    shortURL = ''

    for i in range(6):
        shortURL =shortURL+ ''.join(random.choice(letters))
    return JsonResponse({"shortURL": shortURL, "response": "success"})
