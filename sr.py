import time
from requests import get, post
import os
import sys
import requests

def get_tianhang():
    
    url = 'http://api.tianapi.com/weibohot/index?key=f841d49aefd15af36eb082296b5aab9f'
    res = get(url)
    
    content = res.json()
    
    name = content['newslist']
    
    i = 0
    list_tem=[]
    for each in name:
        i+=1
        list_tem.append(each['hotword'])
    print(list_tem)
    d1=list_tem[0]
    d2=list_tem[1]
    d3=list_tem[2]
    d4=list_tem[3]
    d5=list_tem[4]
    d6=list_tem[5]
    d7=list_tem[6]
    d8=list_tem[7]
    d9=list_tem[8]
    d10=list_tem[9]
    return d1,d2,d3,d4,d5,d6,d7,d8,d9,d10
def get_access_token():
    # appId 
    app_id = config["app_id"]
    # appSecret
    app_secret = config["app_secret"]
    post_url = ("https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid={}&secret={}"
                .format(app_id, app_secret))
    try:
        access_token = get(post_url).json()['access_token']
    except KeyError:
        print("获取access_token失败，请检查app_id和app_secret是否正确")
        os.system("pause") 
        sys.exit(1)
    # print(access_token)
    return access_token

def send_message(access_token,to_user,d1,d2,d3,d4,d5,d6,d7,d8,d9,d10):
    url = "https://api.weixin.qq.com/cgi-bin/message/template/send?access_token={}".format(access_token)
    data = {
        "touser": to_user,
        "template_id": config["template_id"],
        "url": "http://weixin.qq.com/download",
        "data": {
            "d1": {
                "value": d1,
                "color": "#F44336"
            },
            "d2": {
                "value": d2,
                "color": "#F44336"
            },
            "d3": {
                "value": d3,
                "color": "#F44336"
            },
            "d4": {
                "value": d4
                
            },
            "d5": {
                "value": d5
                
            },
            "d6": {
                "value": d6
                
            },
            "d7": {
                "value": d7
                
            },
            "d8": {
                "value": d8
               
            },
            "d9": {
                "value": d9
                
            },
            "d10": {
                "value": d10
                
            }
        }
    }
    headers = {
        'Content-Type': 'application/json',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                      'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
    }
    response = post(url, headers=headers, json=data).json()
    if response["errcode"] == 40037:
        print("推送消息失败，请检查模板id是否正确")
    elif response["errcode"] == 40036:
        print("推送消息失败，请检查模板id是否为空")
    elif response["errcode"] == 40003:
        print("推送消息失败，请检查微信号是否正确")
    elif response["errcode"] == 0:
        print("推送消息成功")
    else:
        print(response)
if __name__ == "__main__":
    try:
        with open("config.txt", encoding="utf-8") as f:
            config = eval(f.read())
    except FileNotFoundError:
        print("推送消息失败，请检查config.txt文件是否与程序位于同一路径")
        os.system("pause")
        sys.exit(1)
    except SyntaxError:
        print("推送消息失败，请检查配置文件格式是否正确")
        os.system("pause")
        sys.exit(1)
d1,d2,d3,d4,d5,d6,d7,d8,d9,d10=get_tianhang()
accessToken = get_access_token()
users = config["user"]
for user in users:
    send_message(accessToken,user,d1,d2,d3,d4,d5,d6,d7,d8,d9,d10)
    os.system("pause")