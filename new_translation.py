# 네이버 Papago Text Translation API 예제(유료)
import os
import sys
import urllib.request
import json

papago_client_id = ""
papago_client_secret = ""
# encText = urllib.parse.quote("번역할 문장 입력")
# data = "source=ko&target=en&text=" + encText
# url = "https://naveropenapi.apigw.ntruss.com/nmt/v1/translation"
# request = urllib.request.Request(url)
# request.add_header("X-NCP-APIGW-API-KEY-ID",papago_client_id)
# request.add_header("X-NCP-APIGW-API-KEY",papago_client_secret)
# response = urllib.request.urlopen(request, data=data.encode("utf-8"))
# rescode = response.getcode()
# if(rescode==200):
#     response_body = response.read()
#     str_to_json = json.loads(response_body.decode('utf-8'))
#     print(str_to_json['message']['result']['translatedText'])
# else:
#     print("Error Code:" + rescode)

def papago_ko_en(sentence):
    encText = urllib.parse.quote(sentence)
    data = "source=ko&target=en&text=" + encText
    url = "https://naveropenapi.apigw.ntruss.com/nmt/v1/translation"
    request = urllib.request.Request(url)
    request.add_header("X-NCP-APIGW-API-KEY-ID",papago_client_id)
    request.add_header("X-NCP-APIGW-API-KEY",papago_client_secret)
    response = urllib.request.urlopen(request, data=data.encode("utf-8"))
    rescode = response.getcode()
    if(rescode==200):
        response_body = response.read()
        str_to_json = json.loads(response_body.decode('utf-8'))
        return str_to_json['message']['result']['translatedText']
    else:
        print("Error Code:" + rescode)


def papago_en_ko(sentence):
    encText = urllib.parse.quote(sentence)
    data = "source=en&target=ko&honorific=True&text=" + encText
    url = "https://naveropenapi.apigw.ntruss.com/nmt/v1/translation"
    request = urllib.request.Request(url)
    request.add_header("X-NCP-APIGW-API-KEY-ID",papago_client_id)
    request.add_header("X-NCP-APIGW-API-KEY",papago_client_secret)
    response = urllib.request.urlopen(request, data=data.encode("utf-8"))
    rescode = response.getcode()
    if(rescode==200):
        response_body = response.read()
        str_to_json = json.loads(response_body.decode('utf-8'))
        return str_to_json['message']['result']['translatedText']
    else:
        print("Error Code:" + rescode)