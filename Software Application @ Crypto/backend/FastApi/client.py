# client
import socket
from utils import mess_enc, mess_dec
from server import message_list, run

server_IP = "127.0.0.1"
server_Port = 5005
bufferSize = 2048
dec_message_list = []


def sender(name_pw, message):
    try:
        if run==False:
            return False
        key = "0123456789101112"
        UDP_client_socket = socket.socket(
            family=socket.AF_INET, type=socket.SOCK_DGRAM)
        message = mess_enc(message, key)
        message = f'{name_pw}+' + message
        UDP_client_socket.sendto(message.encode(
            "utf-8"), (server_IP, server_Port))
        UDP_client_socket.close()
        return True
    except:
        return False


def receiver():
    key = "0123456789101112"
    global dec_message_list
    dec_message_list = []
    for mess in range(len(message_list)):
        name, enc_message = message_list[mess].split("+")
        dec_mess = mess_dec(enc_message, key)
        message = f'[{name}]::>{dec_mess}'
        dec_message_list.append(message)
    return dec_message_list
