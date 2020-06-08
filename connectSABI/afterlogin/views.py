from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
# Create your views here.
def login(request):

    loginusername = request.POST['loginusername']
    loginpassword = request.POST['loginpassword']
    user = auth.authenticate(username=loginusername,password=loginpassword)
    # print(loginusername,loginpassword)
    if user is not None:
        auth.login(request,None)
        return render(request,'afterlogin/home.html')
    else:
        # print("I am here")
        messages.info(request,'invalid credentials')
        return redirect('/')