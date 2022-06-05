import hashlib
import time
import urllib
import requests
import smtplib
import datetime
import platform
from email.mime.text import MIMEText
from email.utils import formataddr


requests.packages.urllib3.disable_warnings()
# CK = 'e5fe7daab1b64929981cd4ddc38d232c' 2022-04-24过期
CK = '407714a4ad78495393ec386b919f1c8d'
sign_time = int(round(time.time()*1000))
content = f'四川省_{sign_time}_成都市'
para = {
	'answers': '["0","0","0","0","2","0","1","1","0","1"]',
	'latitude': '30.82404',
	'longitude': '104.15801',
	'country': '中国',
	'city': '成都市',
	'district': '新都区',
	'province': '四川省',
	'township': '新都街道',
	'street': '上升街',
	'areacode': '510114',
	'towncode': '510114003',
	'citycode': '156510100',
	'timestampHeader': sign_time,
	'signatureHeader': hashlib.sha256(content.encode('utf8')).hexdigest()
}

src = urllib.parse.urlencode(para)
UA = 'Mozilla/5.0 (iPhone;CPU iPhone OS15_0_1 like Mac OS X)AppleWebKit/605.1.15(KHTML,like Gecko)Mobile/15E148MicroMessenger/8.0.10(0x18000a2a)NetType/WIFILanguage/zh_CN'
url = 'https://student.wozaixiaoyuan.com/health/save.json'
pushtype = 'application/x-www-form-urlencoded;charset=UTF-8'
header = {'UserAgent': UA, 'JWSESSION': CK, 'Content-Type': pushtype}
res = requests.post(url, data=src, headers=header, verify=False)
code = res.status_code
if code == '200':
    print('RESULT:', res.text)
    print('STATUS:', res.status_code)
else:
    print('RESULT:', res.text)
    print('STATUS:', res.status_code)


my_sender = '2909270745@qq.com'  # 填写发信人的邮箱账号
my_pass = 'dekbhmciiyjudfea'  # 发件人邮箱授权码
my_user = '201931041416@stu.swpu.edu.cn'  # 收件人邮箱账号
title = res.text
cont = f'''状态码 {res.status_code}
内容 {res.text}
日期 {datetime.datetime.now()}
Python版本 {platform.python_version()}
操作系统可执行程序的结构 {platform.architecture()}
计算机的网络名称 {platform.node()}
操作系统名称及版本号 {platform.platform()}
计算机处理器信息 {platform.processor()}
操作系统中Python的构建日期 {platform.python_build()}
系统中python解释器的信息 {platform.python_compiler()}
操作系统的版本 {platform.version()}'''

def mail():
    ret = True
    try:
        msg = MIMEText(cont, 'plain', 'utf-8')  # 填写邮件内容
        msg['From'] = formataddr([res.text, my_sender])  # 括号里的对应发件人邮箱昵称、发件人邮箱账号
        msg['To'] = formataddr([res.text, my_user])  # 括号里的对应收件人邮箱昵称、收件人邮箱账号
        msg['Subject'] = title  # 邮件的主题，也可以说是标题

        server = smtplib.SMTP_SSL("smtp.qq.com", 465)  # 发件人邮箱中的SMTP服务器
        server.login(my_sender, my_pass)  # 括号中对应的是发件人邮箱账号、邮箱授权码
        server.sendmail(my_sender, [my_user, ], msg.as_string())  # 括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
        server.quit()  # 关闭连接
    except Exception:  # 如果 try 中的语句没有执行，则会执行下面的 ret=False
        ret = False
    return ret


ret = mail()
if ret:
    print("邮件发送成功")
else:
    print("邮件发送失败")
