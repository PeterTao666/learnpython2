import socket

def tcp_srv():
    # 1.建立socket负责具体通信，这个socket其实只负责请求，真正通信的是连接后的
    # 需要用到两个参数
    # AF_INET:含义用UDP一致
    # SOCK_STREAM:表明是使用TCP进行通信
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 2.绑定端口地址
    # 此地址信息是一个元组类型被容，元组分两个部分，第一部分为字符串，代表IP，第二部分为端口
    addr = ("127.0.0.1", 8998)
    sock.bind(addr)

    # 3.监听接入的访问socket
    sock.listen()

    while True:
        # 4.接受访问的socket，可以理解接受访问即建立了一个通讯的链接通路
        # accept返回的元组第一个元素赋值给skt，第二个赋值给addr
        skt,addr = sock.accept()

        # 5.接受对方的发送内容，利用接收到的socket接收内容
        # 500代表接收使用的buffersize
        # msg = skt.receive(500)
        msg = skt.recv(500)
        # 接收到的是bytes格式内容
        # 想得到str格式的，需要进行解码
        msg = msg.decode()

        rst = "Received msg:{0} from {1}".format(msg, addr)
        print(rst)
        # 6.如果有必要，给对方发送反馈信息
        skt.send(rst.encode())

        # 7.关闭连接通路
        skt.close()

if __name__ == "__main__":
    print("Starting TCP sever......")
    tcp_srv()
    print("Ending TCP sever......")