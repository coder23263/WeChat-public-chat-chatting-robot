# -*- coding: utf-8 -*-
# filename: menu.py
# 注意：由于微信公众平台对2014年之后的个人订阅号（个人）不再提供微信认证，而未经认证的个人订阅号无法进行开发模式下的菜单的自定义的创建，\
# 会报错！需要有认证的公众号才能进行开发模式的自定义菜单的创建，参考见http://kf.qq.com/faq/161219MNZRfm161219eIvY7Z.html，导致无法调用自定义菜单接口，
# 从而无法创建！在此不得不说腾讯圈钱的路子深啊，这一举措玩的真优雅，所以你得花300RMB。

import urllib.request
from basic import Basic
import requests

class Menu(object):
    def __init__(self):
        pass

    def create(self, postData, accessToken):
        postUrl = "https://api.weixin.qq.com/cgi-bin/menu/create?access_token=%s" % accessToken
        if isinstance(postData, str):
            postData = postData.encode('utf-8')
        ans = requests.post(postUrl, data=postData)
        print(ans.text)

    def query(self, accessToken):
        postUrl = "https://api.weixin.qq.com/cgi-bin/menu/get?access_token=%s" % accessToken
        urlResp = urllib.request.urlopen(url=postUrl)
        print(urlResp.read())

    def delete(self, accessToken):
        postUrl = "https://api.weixin.qq.com/cgi-bin/menu/delete?access_token=%s" % accessToken
        urlResp = urllib.request.urlopen(url=postUrl)
        print(urlResp.read())

    # 获取自定义菜单配置接口
    def get_current_selfmenu_info(self, accessToken):
        postUrl = "https://api.weixin.qq.com/cgi-bin/get_current_selfmenu_info?access_token=%s" % accessToken
        urlResp = urllib.request.urlopen(url=postUrl)
        print(urlResp.read())


if __name__ == '__main__':
    myMenu = Menu()
    postJson = """
    {
        "button":
        [
            {
                "type": "click",
                "name": "开发指引",
                "key":  "mpGuide"
            },
            {
                "name": "公众平台",
                "sub_button":
                [
                    {
                        "type": "view",
                        "name": "更新公告",
                        "url": "http://mp.weixin.qq.com/wiki?t=resource/res_main&id=mp1418702138&token=&lang=zh_CN"
                    },
                    {
                        "type": "view",
                        "name": "接口权限说明",
                        "url": "http://mp.weixin.qq.com/wiki?t=resource/res_main&id=mp1418702138&token=&lang=zh_CN"
                    },
                    {
                        "type": "view",
                        "name": "返回码说明",
                        "url": "http://mp.weixin.qq.com/wiki?t=resource/res_main&id=mp1433747234&token=&lang=zh_CN"
                    }
                ]
            },
            {
                "type": "media_id",
                "name": "旅行",
                "media_id": "z2zOokJvlzCXXNhSjF46gdx6rSghwX2xOD5GUV9nbX4"
            }
          ]
    }
    """
    accessToken = Basic().get_access_token()
    #print(accessToken)
    # myMenu.delete(accessToken)
    myMenu.create(postJson, accessToken)