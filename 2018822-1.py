# -*- coding: utf-8 -*-
"""
Created on Wed Aug 22 12:32:19 2018

@author: xcy
"""
import time
import itchat
import requests

def auto_response(msg):
    apiUrl = 'http://www.tuling123.com/openapi/api'
    data = {
            'key':'3ac6f6689d27409e8afd2a71ca5f813e',
            'info':msg,
            'userid':'312994'
            }
    r = requests.post(apiUrl,data=data).json()
    return r.get('text')

@itchat.msg_register(itchat.content.TEXT)
def auto_reply(msg):
    if msg['FromUserName'] == myUserName:
        itchat.send_msg(u'[{0}]收到好友@{1}的信息：{2}\n'.format(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(msg['CreateTime'])), msg['User']['NickName'],msg['Text']), 'filehelper')
    return '🤖：'+auto_response(msg['Text'])

if __name__ == '__main__':
    itchat.auto_login()
    myUserName = itchat.search_friends( remarkName='', nickName='ly')[0]['UserName']
    itchat.run()