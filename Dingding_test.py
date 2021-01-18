import requests


import time
import hmac
import hashlib
import base64
import urllib.parse

timestamp = str(round(time.time() * 1000))
secret = 'SEC46add82af58094e4aded6adf7abdd4ad884cbb9c104949390e231aa2363cdc72'
secret_enc = secret.encode('utf-8')
string_to_sign = '{}\n{}'.format(timestamp, secret)
string_to_sign_enc = string_to_sign.encode('utf-8')
hmac_code = hmac.new(secret_enc, string_to_sign_enc, digestmod=hashlib.sha256).digest()
sign = urllib.parse.quote_plus(base64.b64encode(hmac_code))
print(timestamp)
print(sign)


url = "https://oapi.dingtalk.com/robot/send?access_token=3624aa6b4efffaf911b8ba332494c892135dd59b3ca51b711f941c252857440b&timestamp={}&sign={}".format(timestamp,sign)

print(url)

sendmsg = {
    "msgtype": "markdown",
    "markdown": {
        "title": "任务失败告警",
        "text":"attention"
    }
}

def sendMsg(sendmsg):
    req = requests.post(url, json=sendmsg)

    result = req.json()
    if result['errcode'] != 0:
        print('notify dingtalk error: %s' % result['errcode'])

sendMsg(sendmsg)


