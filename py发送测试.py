import socket;

Run = 1

while Run < 2:
    portArm = input("发送地址：")
    portArmP = input("发送端口：")
    try:
        socket1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        socket1.connect((portArm, int(portArmP)))
        message = input("请输入要发送的文字：")
        message = message.encode()
        socket1.sendall(message)

        socket1.close()

        Run = input("是否继续【不输入默认继续】")

        if Run == "" or Run == "y" or Run == "Y" or Run == "yes" or Run == "Yes":
            Run = 1
        else:
            Run  = 10
    except socket.error as e:
        print("连接不到服务器: ", e)

print("程序结束")



