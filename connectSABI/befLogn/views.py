from django.shortcuts import redirect, render
from django.core.mail import send_mail
from django.contrib import messages
from connectSABI import settings
from random import random
from . import forms
# Create your views here.


def index(request):
    return render(request, 'befLogn/index.html')


def register(request):
    regEmail = request.POST.get('registerEmail')
    otp = int(1000000*random())
    print('User Email: ', settings.EMAIL_HOST_USER)
    print('User Password: ', settings.EMAIL_HOST_PASSWORD)
    form = forms.OTPform()
    context = {
        'form': form,
        'name': 'Akarsh'
    }
    mailer('SABI Confirmation', 'This is your OTP: '+str(otp), regEmail)
    return render(request, 'register.html', context)


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

    