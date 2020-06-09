from django.shortcuts import redirect, render
from django.core.mail import send_mail
from django.contrib import messages
from django.contrib.auth.models import auth, User
from connectSABI import settings
from random import random
from . import forms
# Create your views here.


def index(request):
    return render(request, 'befLogn/index.html')


def register(request):
    regEmail = request.GET.get('registerEmail')
    form = forms.Signupform()
    context = {
        'form': form,
        'pMatch': True,
        'uName': False
    }
    if request.method == 'POST':
        form = forms.Signupform(request.POST)
        if form.is_valid():
            fName = form.cleaned_data['fName']
            lName = form.cleaned_data['lName']
            uName = form.cleaned_data['uName']
            password = form.cleaned_data['password']
            cpassword = form.cleaned_data['cpassword']
            if(password != cpassword):
                context['pMatch'] = False
            elif User.objects.filter(username=uName).exists():
                context['uName'] = True
            else:
                user = User.objects.create_user(
                    username=uName, password=password, email=regEmail, first_name=fName, last_name=lName)
                user.save()
                # redirect to a new URL:
                context['success'] = True

    return render(request, 'befLogn/register.html', context)


def mailer(subject, content, receiver):
    v = send_mail(subject, content, 'akarshreceives@gmail.com',
                  [receiver], fail_silently=False)
    print('No. of emails sent: ', v)


# testing page, in case ypu want to test an html file
def formCheck(request):
    form = forms.OTPform()
    context = {
        'form': form,
        'name': 'Akarsh'
    }
    return render(request, 'confirmationPage.html', context)
