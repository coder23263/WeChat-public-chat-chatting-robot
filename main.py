# -*- coding: utf-8 -*-
import web
from handle import Handle
# main.py 运行程序：sudo python3 main.py 80
# handle.py 逻辑处理函数，处理粉丝对服务器的post or get请求
# receive.py 服务器接收粉丝消息的函数，对其进行预处理
# reply.py 服务器返回给粉丝消息的函数
# basic.py 获取accessToken的函数
# media.py 临时添加，下载素材的函数
# menu.py 这个函数未经测试，是设计自定义菜单的函数


urls = (
            '/wx/', 'Handle',
            )



if __name__ == '__main__':
    app = web.application(urls, globals())
    app.run()
