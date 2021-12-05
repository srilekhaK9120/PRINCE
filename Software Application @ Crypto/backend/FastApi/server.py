import socket
from threading import Thread
from utils import known_user
bufferSize = 2048
message_list = []
run = True


def server_thread():
    global run
    run = True
    UDP_IP = "127.0.0.1"
    UDP_PORT = 5005
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.bind((UDP_IP, UDP_PORT))
        print("[+]Group Chat Application Server up and running")
    except:
        print("Server not created!")
        s.close()
    try:
        while run:
            message, _ = s.recvfrom(bufferSize)
            if message:
                message = message.decode("utf-8")
                name, pw, enc_message = message.split('+')
                if known_user(name, pw):
                    if run:
                        message = f'{name}+' + enc_message
                        message_list.append(message)

        print("out of loop, server stoped completely")
    except:
        print('"server stopped due to exception": "yes[++]"')


def server_call():
    t = Thread(target=server_thread)
    t.start()
    t.join()


def server_stop():
    global run
    run = False
    print("server stopped")
