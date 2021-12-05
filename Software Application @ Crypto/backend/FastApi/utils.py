import hashlib
import prince


def mess_enc(message, key):
    # key should be 16 lettered string
    # binary conversion of key
    key_bin_rep = ''.join(format(ord(i), '08b') for i in key)
    # hexadecimal conversion of key
    key_hex_rep = ""
    for i in range(0, len(key_bin_rep), 4):
        key_hex_rep += hex(int(key_bin_rep[i:i+4], 2))[2:]
    key = key_hex_rep
    # Extra Text
    y = (len(message)*2) % 16
    if y != 0:
        x = int((16-y)/2)
        extra_text = 'c'*x
        message = message + extra_text
    # binary conversion
    bin_rep = ''.join(format(ord(i), '08b') for i in message)
    # hexadecimal conversion
    hex_rep = ""
    for i in range(0, len(bin_rep), 4):
        hex_rep += hex(int(bin_rep[i:i+4], 2))[2:]
    # encryption of hexadecimal message, 16 at a time
    enc_message = ""
    for i in range(0, len(hex_rep), 16):
        enc_message += prince.prince_encrypter(hex_rep[i:i+16], key)
    # # binary conversion
    # bin_enc_rep = "".join([format(int(i, 16), '04b') for i in enc_message])
    # # conversion to charecters
    # final_enc_message = ""
    # for i in range(0, len(bin_enc_rep), 8):
    #     final_enc_message += chr(int(bin_enc_rep[i:i+8], 2))
    return enc_message
    # return final_enc_message


def mess_dec(message, key):
    # key should be 16 lettered string
    # binary conversion of key
    key_bin_rep = ''.join(format(ord(i), '08b') for i in key)
    # hexadecimal conversion of key
    key_hex_rep = ""
    for i in range(0, len(key_bin_rep), 4):
        key_hex_rep += hex(int(key_bin_rep[i:i+4], 2))[2:]
    key = key_hex_rep
    # ###### message to hex ######
    # # binary conversion
    # bin_rep = ''.join(format(ord(i), '08b') for i in message)
    # # hexadecimal conversion
    # hex_rep = ""
    # for i in range(0, len(bin_rep), 4):
    #     hex_rep += hex(int(bin_rep[i:i+4], 2))[2:]
    # decryption of hexadecimal message
    dec_message = ""
    for i in range(0, len(message), 16):       # message below
        dec_message += prince.prince_decrypter(message[i:i+16], key)
    # binary conversion
    bindec_rep = "".join([format(int(i, 16), '04b') for i in dec_message])
    # conversion to original message
    original_message = ""
    for i in range(0, len(bindec_rep), 8):
        original_message += chr(int(bindec_rep[i:i+8], 2))
    # deleting trailing "c"s
    for _ in range(1, len(original_message)+1):
        if original_message[-1] == "c":
            original_message = original_message[:-1]
        else:
            break
    return original_message


client_list = ['srilekha', 'vivek', 'kishore', 'guest1', 'guest2']
real_pwd = ['abc', '123', 'abc123', 'guest1', 'guest2']
# hash used is sha256 from SHA-2
hash_pw_list = ['ba7816bf8f01cfea414140de5dae2223b00361a396177a9cb410ff61f20015ad', 'a665a45920422f9d417e4867efdc4fb8a04a1f3fff1fa07e998e86f7f7a27ae3',
                '6ca13d52ca70c883e0f0bb101e425a89e8624de51db2d2392593af6a84118090', '4676424d5f805a7579abd1236287be2abf24f39b8a622ef587edd7d91b8e2952', '5be6ba1446ed4bd41b656b740eccab74524602bc5f274e03677b6bab7d424dd5']


def hash(pwd):
    return hashlib.sha256(pwd.encode()).hexdigest()


def known_user(name, pwd):
    for i in range(len(client_list)):
        if (name == client_list[i] and hash(pwd) == hash_pw_list[i]):
            return True
    return False


def new_user_registration(name, pwd):
    try:
        client_list.append(name)
        hash_pw_list.append(hash(pwd))
        return True
    except:
        return False
