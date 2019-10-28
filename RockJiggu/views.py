from django.shortcuts import render,redirect,get_object_or_404
# CSRF
from django.views.decorators.csrf import csrf_exempt

from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.core.mail import EmailMessage
from django.utils.encoding import force_bytes, force_text
from django.core.mail import BadHeaderError, send_mail
from django.http import HttpResponse, HttpResponseRedirect

def home(request):
    return render(request, 'index.html') 

def contact(request):
    return render(request, 'contact.html')

@csrf_exempt
def sendemail(request):
    username = request.POST.get('username')
    subject = "돌직구 사용자"+ username+ "님이 보내신 문의 메일입니다."
    message = request.POST.get('message')
    useremail = request.POST.get("useremail")
    if subject and message and useremail:
        try:
            send_mail(subject, message, useremail, ["rockjiggu16@gmail.com"])
        except BadHeaderError:
            return HttpResponse('Invalid header found.')
        return redirect('home')
    else:
        return HttpResponse("정확하게 입력해주세요.")        


