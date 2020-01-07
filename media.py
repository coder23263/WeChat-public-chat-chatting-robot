# -*- coding: utf-8 -*-
# filename: media.py
from basic import Basic
import urllib.request
import poster3.encode
import urllib
from poster3.streaminghttp import register_openers
import json
import requests

class Media(object):
    def __init__(self):
        register_openers()

    def upload(self, accessToken, filePath, mediaType):#上传图片
        openFile = open(filePath, "rb")
        param = {'media': openFile}
        postUrl = "https://api.weixin.qq.com/cgi-bin/media/upload?access_token=%s&type=%s" % (accessToken, mediaType)
        ans = requests.post(postUrl, files=param)
        print(ans.text)

    def get(self, accessToken, mediaId):
        postUrl = "https://api.weixin.qq.com/cgi-bin/media/get?access_token=%s&media_id=%s" % (accessToken, mediaId)
        urlResp = urllib.request.urlopen(postUrl)
        print(urlResp.info().__dict__)
        headers = urlResp.info().__dict__['_headers']
        if ('Content-Type: application/json\r\n' in headers) or ('Content-Type: text/plain\r\n' in headers):
            jsonDict = json.loads(urlResp.read())
            print(jsonDict)
        else:
            buffer = urlResp.read()   #素材的二进制
            with open("test_media.jpg", "wb") as fp:
                fp.write(buffer)
            print("get successful")

if __name__ == '__main__':
    myMedia = Media()
    accessToken = Basic().get_access_token()
    filePath = "1.jpg"   #请安实际填写
    mediaType = "image"
    #myMedia.upload(accessToken, filePath, mediaType)
    myMedia.get(accessToken, mediaId="3rD2Sg7ChTZE6UEaDsuzlWtPdAayJMSx1Bd-wBXvFFG6ontWBG9luU8OE96bTl5M")

