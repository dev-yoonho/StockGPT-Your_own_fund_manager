# 파파고 무료 버전
# import os
# import sys
# import urllib.request
# import json

# papago_client_id = "" # 개발자센터에서 발급받은 Client ID 값
# papago_client_secret = "" # 개발자센터에서 발급받은 Client Secret 값

# def papago_ko_en(sentence):
#     encText = urllib.parse.quote(sentence)
#     data = "source=ko&target=en&text=" + encText
#     url = "https://openapi.naver.com/v1/papago/n2mt"
#     request = urllib.request.Request(url)
#     request.add_header("X-Naver-Client-Id",papago_client_id)
#     request.add_header("X-Naver-Client-Secret",papago_client_secret)
#     response = urllib.request.urlopen(request, data=data.encode("utf-8"))
#     rescode = response.getcode()
#     if(rescode==200):
#         response_body = response.read()
#         str_to_json = json.loads(response_body.decode('utf-8'))
#         return str_to_json['message']['result']['translatedText']
#     else:
#         print("Error Code:" + rescode)


# def papago_en_ko(sentence):
#     encText = urllib.parse.quote(sentence)
#     data = "source=en&target=ko&text=" + encText
#     url = "https://openapi.naver.com/v1/papago/n2mt"
#     request = urllib.request.Request(url)
#     request.add_header("X-Naver-Client-Id",papago_client_id)
#     request.add_header("X-Naver-Client-Secret",papago_client_secret)
#     response = urllib.request.urlopen(request, data=data.encode("utf-8"))
#     rescode = response.getcode()
#     if(rescode==200):
#         response_body = response.read()
#         str_to_json = json.loads(response_body.decode('utf-8'))
#         return str_to_json['message']['result']['translatedText']
#     else:
#         print("Error Code:" + rescode)

