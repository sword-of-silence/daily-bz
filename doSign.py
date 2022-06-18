from email import message
import json
import logging
import requests, time
import smtplib
import re
from email.mime.text import MIMEText
from email.utils import formataddr

# ck = '901db577025f4060b166a0f66fb8a9f1'
# ck = '9c966d0709d6417181e658956929d77e'
ck = '9431a17bd18a4c7398edcd59779579ae'
getheaders = {
            "Host": "student.wozaixiaoyuan.com",
            "content-type": "application/x-www-form-urlencoded",
            "Accept-Encoding": "gzip, deflate, br",
            "Connection": "keep-alive",
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36 MicroMessenger/7.0.9.501 NetType/WIFI MiniProgramEnv/Windows WindowsWechat",  # 修改4：User-Agent
            "Referer": "https://gw.wozaixiaoyuan.com/h5/mobile/basicinfo/index?jwenv=3&miniAppId=wxce6d08f781975d91&appVersion=1.0.18",  # 修改5：Referer
            "JWSESSION": ck, #修改6：JWSESSION
        }
first = 'page=1&size=5'
getapi="http://student.wozaixiaoyuan.com/sign/getSignMessage.json"
getdata=requests.post(getapi,headers=getheaders,data=first,).json()
time.sleep(1)
getdata=getdata['data']
a=str(getdata).replace("[", "")
b=str(a).replace("]", "")
c=b
d=re.findall(r"{(.+?)}",c)
e="{"+d[0]+"}"
e=eval(e)
Fid=e['id']
Lid=e['logId']
realdata='{"id":'+Lid+","+'"signId":'+Fid+","+'''
"latitude":30.827499,
"longitude":104.187673,
"country":"中国",
"province":"四川省",
"city":"成都市",
"district":"新都区",
"township":"新都街道"'''+"}"#修改7：打卡位置

api="http://student.wozaixiaoyuan.com/sign/doSign.json/"
signheaders={
        "Host": "student.wozaixiaoyuan.com",
        "Content-Type": "application/json",
        "Accept-Encoding": "gzip, deflate, br",
        "Connection": "keep-alive",
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36 MicroMessenger/7.0.9.501 NetType/WIFI MiniProgramEnv/Windows WindowsWechat",  # 修改4：User-Agent
        "Referer": "https://gw.wozaixiaoyuan.com/h5/mobile/basicinfo/index?jwenv=3&miniAppId=wxce6d08f781975d91&appVersion=1.0.18",  # 修改5：Referer
        "JWSESSION": ck, #修改6：JWSESSION
    }
res = requests.post(api, headers=signheaders, data=realdata.encode(),).json()
time.sleep(1)
if res['code']==0:
    print('打卡成功')
else:
    print('打卡失败')
time.sleep(3)
