# -*- coding: utf-8 -*-

import hashlib
import web
import receive
import reply
import requests
import json
import urllib.request
import re


class Handle(object):
    def GET(self):
        try:
            data = web.input()
            if len(data) == 0:
                return "hello, this is handle view"
            signature = data.signature
            timestamp = data.timestamp
            nonce = data.nonce
            echostr = data.echostr
            token = "liangshuaikai"

            list = [token, timestamp, nonce]
            list.sort()
            sha1 = hashlib.sha1()
            map(sha1.update, list)
            hashcode = sha1.hexdigest()
            print("handle/GET func: hashcode, signature: ", hashcode, signature)
            if hashcode == signature:
                return echostr
            else:
                return ""
        except:
            return None

    def POST(self):
        try:
            webData = web.data()
            #print("Handle Post webdata is ", webData)
            recMsg = receive.parse_xml(webData)
            if isinstance(recMsg, receive.Msg) and recMsg.MsgType == 'text':
                toUser = recMsg.FromUserName
                fromUser = recMsg.ToUserName
                #get_response(recMsg)
                msgcontent = recMsg.Content.decode('utf-8')
                content = wxrobot(msgcontent)
                # if msgcontent == 'csdn':
                #     content = "https://blog.csdn.net/qq_41663800"
                # else:
                #     content = "this is a test"
                replyMsg = reply.TextMsg(toUser, fromUser, content)
                return replyMsg.send()
            elif recMsg.MsgType == 'image':
                toUser = recMsg.FromUserName
                fromUser = recMsg.ToUserName
                mediaId = recMsg.MediaId
                replyMsg = reply.ImageMsg(toUser, fromUser, mediaId)
                return replyMsg.send()
            else:
                print (r"暂且不处理")
                return "success"
        except:
            return None

def wxrobot(x):
    x = urllib.parse.quote(x)
    link = urllib.request.urlopen(
        "http://nlp.xiaoi.com/robot/webrobot?&callback=__webrobot_processMsg&data=%7B%22sessionId%22%3A%22ff725c236e5245a3ac825b2dd88a7501%22%2C%22robotId%22%3A%22webbot%22%2C%22userId%22%3A%227cd29df3450745fbbdcf1a462e6c58e6%22%2C%22body%22%3A%7B%22content%22%3A%22" + x + "%22%7D%2C%22type%22%3A%22txt%22%7D")
    html_doc = link.read().decode()
    reply_list = re.findall(r'\"content\":\"(.+?)\\r\\n\"', html_doc)
    # print("小i：" + reply_list[-1])
    # print(reply_list)
    rcontent = reply_list[-1].replace('小i','小梁')
    return rcontent



# 获得图灵机器人回复
# 需要传入两个参数，Msg内容是文本或者表情，返回值就是回复内容
# Key是接入图灵机器人需要的秘钥，需要自己到官网获取

def get_response(Msg, Key = '8be838126c3a7511', Userid='ItChat'):
    url = 'http://www.tuling123.com/openapi/api'
    payloads = {
        'key': Key,
        'info': Msg,
        'userid': Userid,
    }
    try:
        r = requests.post(url, data=json.dumps(payloads)).json()
    except ConnectionError:
        return None
    if not r['code'] in (100000, 200000, 302000, 308000, 313000, 314000):
        return
    if r['code'] == 100000:  # 文本类
        return '\n'.join([r['text'].replace('<br>', '\n')])
    elif r['code'] == 200000:  # 链接类
        return '\n'.join([r['text'].replace('<br>', '\n'), r['url']])
    elif r['code'] == 302000:  # 新闻类
        l = [r['text'].replace('<br>', '\n')]
        for n in r['list']:
            l.append('%s - %s' % (n['article'], n['detailurl']))
        return '\n'.join(l)
    elif r['code'] == 308000:  # 菜谱类
        l = [r['text'].replace('<br>', '\n')]
        for n in r['list']:
            l.append('%s - %s' % (n['name'], n['detailurl']))
        return '\n'.join(l)
    elif r['code'] == 313000:  # 儿歌类
        return '\n'.join([r['text'].replace('<br>', '\n')])
    elif r['code'] == 314000:  # 诗词类
        return '\n'.join([r['text'].replace('<br>', '\n')])
