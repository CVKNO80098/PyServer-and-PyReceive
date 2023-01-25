import socket
import ipinfo
import pickle

access_token = "842d9627d303a4"
handler = ipinfo.getHandler(access_token)
ip_address = handler.getDetails()
PiP = ip_address.ip
PiP = str(PiP)
print("你的公网IP是：",PiP)
print(ip_address.country_name)

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

config = {
    "PublicIP": PiP,
    "test2": ip_address.country_name,
    "test3": get_ip(),
}
print(PiP)
with open("config.pkl", "wb") as f:
    pickle.dump(config, f)
    print("保存完毕")

with open("config.pkl", "rb") as f:
        print("发现config文件，自动使用文件补全信息")
        config = pickle.load(f)
        test1 = config.get('PublicIP')
        test2 = config.get('test2')
        test3 = config.get('test3')
        print(test1)
        print(test2)
        print(test3)