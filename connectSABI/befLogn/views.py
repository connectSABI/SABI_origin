from django.shortcuts import render
from django.core.mail import send_mail
# Create your views here.


def index(request):
    if(request.meth):
    mailer('Hey There!!', 'This is<br> the 2 body', 'ar35@iitbbs.ac.in')
    return render(request, 'index.html')


def mailer(subject, content, receiver):
    v = send_mail(subject, content, 'vanshrana2012@gmail.com',
                  [receiver], fail_silently=False)
    print(v)
