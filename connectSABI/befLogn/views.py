from django.shortcuts import render
from django.core.mail import send_mail
from connectSABI import settings
# Create your views here.


def index(request):
    if request.method == 'POST':
        regEmail = request.POST.get('registerEmail')
        print('User Email: ', settings.EMAIL_HOST_USER)
        mailer('SABI Confirmation', 'This is confirmattion mail', regEmail)
        return render(request, 'confirmationPage.html')
    else:
        return render(request, 'index.html')


def mailer(subject, content, receiver):
    v = send_mail(subject, content, 'vanshrana2012@gmail.com',
                  [receiver], fail_silently=False)
    print('No. of emails sent: ', v)
