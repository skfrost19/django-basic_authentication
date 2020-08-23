from django.contrib import auth
from django.contrib.auth.models import User
from django.shortcuts import render
from firstwebapp.models import Signup, contactus


def Home(request):
    return render(request, 'base.html')


# Signup section

def signup2(request):
    if request.method == 'POST':
        # matching passwords
        if request.POST['password'] == request.POST['passwordRepeat']:
            try:
                user = User.objects.get(username=request.POST['username'])
                return render(request, 'signup2.html', {'fmessage': "Username already exists"})
            except User.DoesNotExist:
                user = User.objects.create_user(username=request.POST['username'], password=request.POST['password'])
                usrname = request.POST['username']
                passwrd = request.POST['password']
                emil = request.POST['email']
                new = Signup(username=usrname, email=emil, password=passwrd)
                new.save()
                return render(request, 'base.html', {'cogmessage': 'Successfully Registered'})
        else:
            return render(request, 'signup2.html', {'erormessage': "Passwords Don't Match"})
    else:
        return render(request, 'signup2.html')


# Login section
def signin(request):
    if request.method == 'POST':
        uname = request.POST['username']
        pwd = request.POST['password']
        # user object creation using given credentials
        user = auth.authenticate(username=uname, password=pwd)
        if user is not None:
            auth.login(request, user)
            return render(request, 'base.html', {'msg': "Successfully Logged-in."})
        else:
            return render(request, 'signin.html', {'signerror': 'Invalid Credentials!!!'})
    else:
        return render(request, 'signin.html')


def AboutUs(request):
    return render(request, 'AboutUs.html')




# contact us handling

def ContactUs(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']

        new_message = contactus(name=name, email_address=email, phone=phone, message=message)
        new_message.save()
        return render(request, 'ContactUs.html', {'contactusmsg': 'Message Sent!!!!'})
    else:
        return render(request, 'ContactUs.html')
