from django.shortcuts import render,redirect,get_object_or_404
# CSRF
from django.views.decorators.csrf import csrf_exempt

from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.core.mail import EmailMessage
from django.utils.encoding import force_bytes, force_text
from django.core.mail import BadHeaderError, send_mail
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.core.mail import EmailMessage
from django.utils.encoding import force_bytes, force_text
from django.contrib import messages
import pdb


def home(request):
    return render(request, 'index.html') 

# def contact(request):
#     return render(request, 'contact.html')

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

@csrf_exempt
def contact(request):
    if request.method == "POST":
        username = request.POST["username"]
        subject = "돌직구 사용자"+ username+ "님이 보내신 문의 메일입니다."
        message = request.POST["message"]
        useremail = request.POST["useremail"]

        emailContent = render_to_string('email.html', {
            "subject": subject,
            "useremail": useremail,
            "message":message,
        })
        emailAddress = "rockjiggu16@gmail.com"
        emailObject = EmailMessage(subject, emailContent, to=[emailAddress])
        emailObject.content_subtype = "html"

        result = emailObject.send()
        if result == 1:
            messages.info(request, "성공적으로 문의가 돌직구에 전달되었습니다.")
        else:
            messgaes.info(request, "문의에 실패하였습니다.")
        return redirect('contact')
    else:
        return render(request, 'contact.html')    

