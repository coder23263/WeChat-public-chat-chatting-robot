# WeChat-public-chat-chatting-robot
基于python3微信公众号陪聊机器人
# 环境配置
1、首先你需要一台服务器，腾讯云，阿里云，xx云都可以
2、配置python环境

```bash
sudo pip3 install web.py
sudo pip3 install urllib
sudo pip3 install poster3
sudo pip3 install requests
```
3、设置服务器安全组规则（自行百度），使得你的服务器开放80端口，或者你想在哪个端口部署你的web应用开放哪个

# 开始部署
```bash
cd wx
sudo python3 main.py 80
```
或者说你想后台部署之：
```bash
cd wx
nohup python3 main.py 80 &
