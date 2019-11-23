from django.shortcuts import render, redirect, get_object_or_404

# JSON
from django.http import JsonResponse
import json
# CSRF
from django.views.decorators.csrf import csrf_exempt
import pdb
from django.core import serializers
from .models import ReturnInfo
from selenium import webdriver



#반품에 필요한 정보들을 저장하는 context입니다.
returninfo_context = "projects/rockjiggu-bot-aivmkh/agent/sessions/b0dd0c37-69a0-0b16-a3b1-ab9300ad668e/contexts/returninfo_context"


@csrf_exempt
def webhook(request):
  print('웹훅')
  req = json.loads(request.body)
  action = req.get('queryResult').get('action')
  params = req.get('queryResult').get('parameters')
  print(action)
  if action == 'self_introduce':
    return self_introduce()
  elif action == 'return_product.return_product-yes':
    return return_product_yes(request) 
  elif action == 'return_product.return_product-no':
    return return_product_no(request) 
  elif action == 'return_product.return_product-yes.return_product-yes-yes': 
    return return_product_yes_yes(request, params)  
  elif action == 'return_product.return_product-yes.return_product-yes-no':
    return return_product_yes_no(request, params)
  elif action == 'return_product.return_product-yes.return_product-yes-yes.return_product-yes-yes-yes':  #선아
    return return_product_yes_yes_yes(request)
  elif action == 'return_product.return_product-yes.return_product-yes-yes.return_product-yes-yes-no':  
    return return_product_yes_yes_no(request)
     


def self_introduce():
  response = {
      'fulfillmentText': '안녕하세요, 저는 해외직구 반품을 도와주는 돌직구 입니다!'
  }
  return JsonResponse(response, safe = False)
  #오류를 피하기 위해 safe = False를 해준다.
 
def create():
  return render(request, 'index.html')


  # is_received = params.get('is_received')
  # returninfo =  ReturnInfo(is_received = is_received)
  # returninfo.save()
  # request.session['returninfo_pk'] = returninfo.objects.latest("pk")


def return_product_yes(request):
  print('asdfasdfasdf')
  request.session['is_received'] = "yes"
  response = {
    'fulfillmentText':'물품을 수령하셨군요!물품을 수령하신 후 반품하실경우 배송대행지 이용여부와 관부가세 납부여부에 따라 절차가 달라집니다! 배송대행지를 이용하셨나요?'
  }
  return JsonResponse(response, safe = False)
  # pk = request.session['returninfo_pk']
  # returninfo = get_object_or_404(ReturnInfo, pk = pk )
  # is_agency = params.get('is_agency')
  # returninfo.is_agency = is_agency
  # returninfo.save()


def return_product_no(request):
  request.session['is_received'] = 'no'
  # pk = request.session['returninfo_pk']
  # returninfo = get_object_or_404(ReturnInfo, pk = pk )
  # is_agency = params.get('is_agency')
  # returninfo.is_agency = is_agency
  # returninfo.save()


def return_product_yes_yes(request, params):
  returninfo = ReturnInfo(is_received = 'yes', is_agency = "yes", agency_name = params.get('agency_name'), mall_name = params.get('mall_name'))
  returninfo.save() 
  response = {
    'fulfillmentText':'관부가세 납부대상이였나요?',
  }
  return JsonResponse(response, safe = False)
  # is_clearance = params.get('is_clearance')
  # request.session = agency_name
  # returninfo.is_clearance = is_clearance
  # returninfo.save()


def return_product_yes_no(request, params):
  returninfo = ReturnInfo(is_received = 'yes', is_agency = "no", mall_name = params.get('mall_name'))
  returninfo.save() 
  response = {
    'fulfillmentText':'관부가세 납부대상이였나요?',
  }
  return JsonResponse(response, safe = False)


def return_product_yes_yes_yes(request):
  returninfo = ReturnInfo.objects.last() 
  returninfo.is_clearance = 'yes'
  returninfo.save()
  if returninfo.agency_name == '이하넥스':
    response = {
      'fulfillmentText': '고객님께서 이용하신 이하넥스의 경우 사전에 위약반송에 필요한 서류(신분증사본, 제1금융권 통장사본, 반품사유서, 셀러와 문답내용, 구매증빙자료)를 준비 후 1:1 반품 게시판으로 문의해주세요.'
    }
    return JsonResponse(response, safe = False)
  else:  
    response = {
      'fulfillmentText' : '고객님꼐서 이용하신 {}를 통해 환불이 가능하지만 수출신고시 발생하는 비용과 환급 신청 수수료는 별도 부담입니다.'.format(returninfo.agency_name),
      "outputContexts": [
              {
                "name": returninfo_context,
                "lifespanCount": 3,
                "parameters": {
                  "order_number": returninfo.id
                }
              }
        ]
    }
    return JsonResponse(response, safe=False)

def return_product_yes_yes_no(request):  
  returninfo = ReturnInfo.objects.last()
  returninfo.is_clearance = 'no'
  returninfo.save()
  if returninfo.agency_name == '뉴욕걸즈':
    response = {
      'fulfillmentText': 'https://www.nygirlz.co.kr/main/customer/qna.php'
    }
  else:
    response = {
      'fulfillmentText' : '반품신청 및 승인-> 수출신고-> 물품발송-> 관세 환급 신청-> 환불과 관세환급',
      "outputContexts": [
              {
                "name": returninfo_context,
                "lifespanCount": 3,
                "parameters": {
                  "order_number": returninfo.id
                }
              }
        ]
    }
  return JsonResponse(response, safe=False)

def return_product_yes_no_yes(request):  
  returninfo = ReturnInfo.objects.last()
  returninfo.is_clearance = 'yes'
  returninfo.save()
  response = {
      'fulfillmentText': '고객님께서 이용하신 이하넥스의 경우 사전에 위약반송에 필요한 서류(신분증사본, 제1금융권 통장사본, 반품사유서, 셀러와 문답내용, 구매증빙자료)를 준비 후 1:1 반품 게시판으로 문의해주세요.'
    }
  return JsonResponse(response, safe = False)


def return_product_yes_no_no(request):
  returninfo = ReturnInfo.objects.last()
  returninfo.is_clearance = 'no'
  returninfo.save()
  response = {
      'fulfillmentText': '고객님께서 이용하신 이하넥스의 경우 사전에 위약반송에 필요한 서류(신분증사본, 제1금융권 통장사본, 반품사유서, 셀러와 문답내용, 구매증빙자료)를 준비 후 1:1 반품 게시판으로 문의해주세요.'
    }
  return JsonResponse(response, safe = False)



def order_create(params):
    
    name = params.get('name')
    content = params.get('content')
    item = Order(name=name, content = content)
    item.save()

    response = {
        'fulfillmentText' : '감사합니다. 주문번호는 {} 입니다.'.format(item.id),
          "outputContexts": [
            {
              "name": order_context,
              "lifespanCount": 3,
              "parameters": {
                "order_number": item.id
              }
            }
      ]
    }
    
    return JsonResponse(response, safe=False)
    
        
def chat(request):
  return render(request, 'chatbot/chat.html')