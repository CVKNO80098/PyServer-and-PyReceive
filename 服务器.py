# -*- coding: utf-8 -*-

import socket
import ipinfo
import pickle

socket2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

initPlan = 1;

try :
    with open("config.pkl", "rb") as f:
        print("发现config文件，自动使用文件补全信息")
        config = pickle.load(f)
        iP = config.get("IP")
        publicIP = config.get("publicIP")
        if iP:

            print("您的IP是：",iP)
            print("您的公网IP是：",publicIP)
            initPlan = 2
        else:
            print("IP not found in config")
            initPlan = 1
except:
    print("未发现config文件或者文件格式错误，将自动生成")
    initPlan = 1

while initPlan == 1:
    locals = input("我们将您的IP地址，我们将生成一个文件来保存这个address，来维持您的联系，这也是您的唯一证明\n如果您希望您在同一个网络下进行联系，获取您的内网IP\n如果您希望连接到服务器，并与互联网连接，请输入公网IP\n如果您不知道如何获取自己的连接，请输入help来显示帮助\n\n请注意！当前使用自动注册服务！自动储存您的公网与内网信息！\n\n")

    #获取内网IP，通过一个错误抛出？
    def get_ip():
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        try:
            # doesn't even have to be reachable
            s.connect(('10.255.255.255', 1))
            IP = s.getsockname()[0]
        except:
            IP = '127.0.0.1'
        finally:
            s.close()
        return IP
    print("您的内网IP为",get_ip())

    #通过ipinfo.io获取详细的公网信息
    access_token = "842d9627d303a4"
    handler = ipinfo.getHandler(access_token)
    ip_address = handler.getDetails()
    print("你的公网IP是：",ip_address.ip)
    #保存到config
    config = {
    "publicIP": ip_address.ip,
    "IP": get_ip(),
    "Country" : ip_address.country_name
    }
    
    with open("config.pkl", "wb") as f:
        pickle.dump(config, f)
        print("请记住您的IP，这是别人与你连接的唯一方法\n")

    initPlan = 2
    iP = get_ip()
    publicIP = ip_address.ip
#注册代码完毕，ip为iP，公网ip为publicIP
loginPlan = input("请输入您的登录方法：\n内网:n\n公网:p\n(均为小写！)")
if loginPlan =="n":
    IPconnect = iP
elif loginPlan =="p":
    IPconnect = publicIP
else:
    print("NO!")
    exit(0)
socket2.bind((IPconnect,8865))
# 监听连接
socket2.listen()
print("[log]server is listening on port 8865")

while True:
    # 接受客户端连接
    client, address = socket2.accept()
    print(f"received connection from {address}")
    message = client.recv(8865)
    message = message.decode() # 将字节类型解码为字符串
    print(f"received message: {message}")

    # 关闭连接
    client.close()

# 关闭服务器
socket2.close()