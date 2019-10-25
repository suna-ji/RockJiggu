from django.shortcuts import render, redirect

# JSON
from django.http import JsonResponse
import json
# CSRF
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def webhook(request):
    if request.method == 'POST':
        req = json.loads(request.body)
        action = req.get('queryResult').get('action')
        params = req.get('queryResult').get('parameters')
        if action == 'self_introduce':
            return self_introduce()
        elif action == 'create':
            return create()    


def self_introduce():
    response = {
        'fulfillmentText': '안녕하세요, 저는 해외직구 반품을 도와주는 돌직구 입니다!'
    }
    return JsonResponse(response, safe = False)
    #오류를 피하기 위해 safe = False를 해준다.
 
def create():
    return render(request, 'index.html')



