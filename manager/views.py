from os import name
import random
from django.http.response import HttpResponse 

from django.shortcuts import redirect, render
from django.contrib.auth.models import User 
from django.contrib.auth import authenticate, login, logout
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages

# Create your views here.

def send_email():
    email_subject = 'DPM verification'
    code = str(random.randint(10000, 999999))
    email_body = f"Your verification code is: {code}"
    to = "sahaib9747@yahoo.com"
    send_mail(
            email_subject,
            email_body,
            settings.EMAIL_HOST_USER,
            [to],
            fail_silently=False
        )
    return code
def ran():
    return random.random()

rand = ran()
def index(request):
    #send_email()
    if request.method == 'POST':
        if 'login-form' in request.POST:
            username = request.POST['username']
            password = request.POST['password']
            # check user
            login = authenticate(username=username, password=password)
            if login is None:
                global security_code 
                security_code = send_email()
            else:
                print('none noy')
                messages.error(request, 'Invalid credentials!')
                return redirect('/')
        elif 'code-submit-form' in request.POST:
            code = request.POST['security-code']
            if code == security_code:
                print('checked')
            else:
                print('wrong code')
        else:
            print(security_code)
    print(rand)     
    print('Name', type(name))          
    return render(request, 'index.html')
print('This is manager.views')
def another():
    global student 
    student = 'DPI'
another()



def index(request):
    return HttpResponse(student)


print('Anyting')