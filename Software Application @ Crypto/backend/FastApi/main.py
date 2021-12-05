from fastapi import FastAPI
from utils import mess_enc, mess_dec, known_user, new_user_registration
from server import server_call, server_stop, message_list
from client import sender, receiver
app = FastAPI()

api_available = ['welcome', 'encrypt', 'decrypt',
                 'start_server(chat_server)', 'stop_server(chat_server)', 'send_message', 'receive_all', 'database', 'register_user']


@app.get("/")
def home_page():
    return {"Welcome_message": "Welcome to Prince Cipher Cryptography", "available_APIs": api_available}

#### encryption and decryption ####


@app.get("/enc/{message}/{key}")
def encrypt(message: str, key: str):
    enc_message = mess_enc(message, key)
    return {"enc_algorithm": "prince", "original_message_to_enc": message, "key_used": key, "encrypted_message": enc_message}


@app.get("/dec/{message}/{key}")
def decrypt(message: str, key: str):
    original_message = mess_dec(message, key)
    return {"enc_algorithm": "prince", "original_message_to_dec": message, "key_used": key, "decrypted_message": original_message}
#### encryption and decryption ####

#### start and stop the server ####


@app.get("/start_server")
def start_server():
    stopped = server_call()
    return stopped


@app.get("/stop")
# stop is required (in lower_case)
def stop_server():
    server_stop()

#### start and stop the server ####


@app.get("/send_message/{name_pw}/{message}")
def send_message(name_pw: str, message: str):
    name, pwd = name_pw.split("+")
    if known_user(name, pwd):
        if sender(name_pw, message):
            return {"sent successful": "[+]"}
    return {"sent successful": "[-]"}


@app.get("/receive_all/{name_pwd}")
def receive_message(name_pwd: str):
    name, pwd = name_pwd.split("+")
    if known_user(name, pwd):
        dec_message_list = receiver()
        return {"all_messages": dec_message_list}
    return {"all_messages": ["You are not an authenticated user!"]}


@app.get("/database/{name_pwd}")
def server_data(name_pwd: str):
    name, pw = name_pwd.split("+")
    if known_user(name, pw):
        return {"server_data": message_list}
    return {"server_data": "You are not an authenticated user!"}


@app.get("/register_user/{name}/{pwd}")
def register_user(name: str, pwd: str):
    if new_user_registration(name, pwd):
        return {"New member created": "[+]"}
    return {"New member created": "[-]"}
