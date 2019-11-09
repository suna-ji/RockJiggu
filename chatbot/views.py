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
        elif action == 'return_product-no-no-custom':
          pass
        elif action == 'return_product-no-yes-clearance':
          pass
        elif action == 'return_product-yes-yes-yes': #선아
          return return_product_yes_yes_yes(params)
        # elif action == 'return_product-yes-yes-no': #선아
        #   return return_product-yes-yse-no(params)     
        # elif action == 'return_product-yes-no-no': #지수
        #   pass
        # elif action == 'return_product-yes-no-yes': #지수
        #   pass         


def self_introduce():
    response = {
        'fulfillmentText': '안녕하세요, 저는 해외직구 반품을 도와주는 돌직구 입니다!'
    }
    return JsonResponse(response, safe = False)
    #오류를 피하기 위해 safe = False를 해준다.
 
def create():
    return render(request, 'index.html')

def chat(request):
    return render(request, 'chatbot/chat.html')

#선아(물품수령 yes -> 배대지 yes->관세 yes)
# 배송대행지를 통해 환불이 가능하지만 수출신고시 발생하는 비용과 환급 신청 수수료는 별도 부담
# 이하넥스의 경우 사전에 위약반송에 필요한 서류준비후 1:1 반품 게시판으로 문의
def return_product_yes_yes_yes(params): 
  agency_name = params.get('agency_name')
  if agency_name == '이하넥스':
    response = {
      'fulfillmentText': '고객님께서 이용하신 {}의 경우, 위약반송에 필요한 서류 1. 신분증 사본 2. 제1금융권 통장사본 3. 반품사유서 4. 셀러와의 문답내용(반품동의서) 5. 구매증빙자료를 사전에 준비하시고 1:1 반품 게시판으로 문의주시면 됩니다.'
    }
    return JsonResponse(response, safe = False)
  else:
    response = {
      'fulfillmentText': '배송대행지를 통해 환불이 가능하지만 수출신고시 발생하는 비용과 환급 신청 수수료는 별도 부담입니다!'
    }
    return JsonResponse(response, safe = False)




#선아
# def return_product_yes_yes_no(params):




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
    
        