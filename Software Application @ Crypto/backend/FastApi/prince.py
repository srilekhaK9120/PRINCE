s_box = {"0": "b", "1": "f", "2": "3", "3": "2", "4": "a", "5": "c", "6": "9", "7": "1",
         "8": "6", "9": "7", "a": "8", "b": "0", "c": "e", "d": "5", "e": "d", "f": "4"}
s_inv = {"0": "b", "1": "7", "2": "3", "3": "2", "4": "f", "5": "d", "6": "8", "7": "9",
         "8": "a", "9": "6", "a": "4", "b": "0", "c": "5", "d": "e", "e": "c", "f": "1"}

Rcon = [[0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0],
                [0x1,0x3,0x1,0x9,0x8,0xa,0x2,0xe,0x0,0x3,0x7,0x0,0x7,0x3,0x4,0x4],
                [0xa,0x4,0x0,0x9,0x3,0x8,0x2,0x2,0x2,0x9,0x9,0xf,0x3,0x1,0xd,0x0],
                [0x0,0x8,0x2,0xe,0xf,0xa,0x9,0x8,0xe,0xc,0x4,0xe,0x6,0xc,0x8,0x9],
                [0x4,0x5,0x2,0x8,0x2,0x1,0xe,0x6,0x3,0x8,0xd,0x0,0x1,0x3,0x7,0x7],
                [0xb,0xe,0x5,0x4,0x6,0x6,0xc,0xf,0x3,0x4,0xe,0x9,0x0,0xc,0x6,0xc],
                [0x7,0xe,0xf,0x8,0x4,0xf,0x7,0x8,0xf,0xd,0x9,0x5,0x5,0xc,0xb,0x1],
                [0x8,0x5,0x8,0x4,0x0,0x8,0x5,0x1,0xf,0x1,0xa,0xc,0x4,0x3,0xa,0xa],
                [0xc,0x8,0x8,0x2,0xd,0x3,0x2,0xf,0x2,0x5,0x3,0x2,0x3,0xc,0x5,0x4],
                [0x6,0x4,0xa,0x5,0x1,0x1,0x9,0x5,0xe,0x0,0xe,0x3,0x6,0x1,0x0,0xd],
                [0xd,0x3,0xb,0x5,0xa,0x3,0x9,0x9,0xc,0xa,0x0,0xc,0x2,0x3,0x9,0x9],
                [0xc,0x0,0xa,0xc,0x2,0x9,0xb,0x7,0xc,0x9,0x7,0xc,0x5,0x0,0xd,0xd]]

def key_as_bin_list(state):
    bin_list = [0 for i in range(4*len(state))]
    i = 0
    for int_val in state:
        # after binary operation it is of form 5-->0b101, so we cut the first 2
        v = bin(int_val)[2:]
        pad_zeros = '0'*(4-len(v))
        v = pad_zeros + v
        # we take every integer value and convert it to 4 bit binary form
        bin_list[i] = int(v[0])
        bin_list[i+1] = int(v[1])
        bin_list[i+2] = int(v[2])
        bin_list[i+3] = int(v[3])
        i = i+4
    return bin_list


def bin_list_to_int(state):
    # make the long binary bit list to a single string
    bit_string = ''.join([str(i) for i in state])
    int_list = []
    # take every 4 bits and convert it to integer
    for i in range(0, len(bit_string), 4):
        int_list.append(int(bit_string[i:i+4], 2))
    return int_list


def key_expansion(key):
    # converting the original key to an array of bits
    key_bin = key_as_bin_list(key)
    # initialize the key to 192 (128-->192)
    final_key = [0]*192
    for i in range(64):
        # original key 64 bits == new key 64 bits
        final_key[i] = key_bin[i]
        # original key last 64 bits == new key last 64 bits
        final_key[i+128] = key_bin[i+64]
    for i in range(63):
        final_key[65+i] = key_bin[i]
    final_key[64] = key_bin[63]
    final_key[127] = final_key[127] ^ key_bin[0]
    return bin_list_to_int(final_key)


def bitwise_xor(v1, v2):
    v3 = []
    for i in range(len(v1)):
        v3.append(v1[i] ^ v2[i])
    return v3


def list_to_hex(state):
    res = ""
    for nibble in state:
        temp = hex(nibble)[2:]
        res += temp
    return res


def sbox(state, box):
    ret = []
    for nibble in state:
        temp = hex(nibble)
        temp = temp[2:]
        ret.append(int(box[temp], 16))
    return ret


def shift_rows(state, inverse):
    ret = [0]*16
    idx = 0
    for nibble in state:
        ret[idx] = nibble
        if not inverse:
            idx = (idx + 13) % 16
        else:
            idx = (idx + 5) % 16
    return ret


def m_0(state):
    mid = [0 for i in range(16)]
    mid[0] = state[4] ^ state[8] ^ state[12]
    mid[1] = state[1] ^ state[9] ^ state[13]
    mid[2] = state[2] ^ state[6] ^ state[14]
    mid[3] = state[3] ^ state[7] ^ state[11]
    mid[4] = state[0] ^ state[4] ^ state[8]
    mid[5] = state[5] ^ state[9] ^ state[13]
    mid[6] = state[2] ^ state[10] ^ state[14]
    mid[7] = state[3] ^ state[7] ^ state[15]
    mid[8] = state[0] ^ state[4] ^ state[12]
    mid[9] = state[1] ^ state[5] ^ state[9]
    mid[10] = state[6] ^ state[10] ^ state[14]
    mid[11] = state[3] ^ state[11] ^ state[15]
    mid[12] = state[0] ^ state[8] ^ state[12]
    mid[13] = state[1] ^ state[5] ^ state[13]
    mid[14] = state[2] ^ state[6] ^ state[10]
    mid[15] = state[7] ^ state[11] ^ state[15]
    return mid


def m_1(state):
    mid = [0]*16
    mid[0] = state[0] ^ state[4] ^ state[8]
    mid[1] = state[5] ^ state[9] ^ state[13]
    mid[2] = state[2] ^ state[10] ^ state[14]
    mid[3] = state[3] ^ state[7] ^ state[15]
    mid[4] = state[0] ^ state[4] ^ state[12]
    mid[5] = state[1] ^ state[5] ^ state[9]
    mid[6] = state[6] ^ state[10] ^ state[14]
    mid[7] = state[3] ^ state[11] ^ state[15]
    mid[8] = state[0] ^ state[8] ^ state[12]
    mid[9] = state[1] ^ state[5] ^ state[13]
    mid[10] = state[2] ^ state[6] ^ state[10]
    mid[11] = state[7] ^ state[11] ^ state[15]
    mid[12] = state[4] ^ state[8] ^ state[12]
    mid[13] = state[1] ^ state[9] ^ state[13]
    mid[14] = state[2] ^ state[6] ^ state[14]
    mid[15] = state[3] ^ state[7] ^ state[11]
    return mid

def hex_to_bin(state):
    ret = [0 for i in range(4*len(state))]
    i = 0
    for nibble in state:
        v = bin(nibble)[2:]
        extra_zeros = '0'*(4-len(v))
        v = extra_zeros+v
        ret[i] = int(v[0])
        ret[i+1] = int(v[1])
        ret[i+2] = int(v[2])
        ret[i+3] = int(v[3])
        i = i+4
    return ret

def mprime(state):
    state = hex_to_bin(state)
    ret = [0 for i in range(64)]
    ret[0:16] = m_0(state[0:16])
    ret[16:32] = m_1(state[16:32])
    ret[32:48] = m_1(state[32:48])
    ret[48:64] = m_0(state[48:64])
    ret = bin_list_to_int(ret)
    return ret


def first5(state, key):
    for idx in range(1, 6):
        state = sbox(state, s_box)
        state = mprime(state)
        state = shift_rows(state, inverse=False)
        state = bitwise_xor(bitwise_xor(Rcon[idx], key), state)
    return state


def last5(state, key):
    for idx in range(6, 11):
        state = bitwise_xor(bitwise_xor(Rcon[idx], key), state)
        state = shift_rows(state, inverse=True)
        state = mprime(state)
        state = sbox(state, s_inv)
    return state


def core(state, key):
    state = bitwise_xor(bitwise_xor(Rcon[0], key), state)
    state = first5(state, key)

    state = sbox(state, s_box)
    state = mprime(state)
    state = sbox(state, s_inv)

    state = last5(state, key)
    state = bitwise_xor(bitwise_xor(Rcon[11], key), state)
    return state

# to print the keys
def print_key(key, name):
    key = [hex(i) for i in key]
    key_hex_string = ''.join(key)
    print(f'{name}: {key_hex_string}')


def prince_encrypter(message, key):
    '''
    first key expansion,
    bitwise xor of k_0 with state,
    core function,
    bitwise xor with (k_0)^'.
    '''
    # storing the message in an array in integer form
    state = [0]*len(message)
    for i in range(len(message)):
        state[i] = int(message[i], 16)
     # storing the key in an array in integer form
    k = [0]*len(key)
    for i in range(len(key)):
        k[i] = int(key[i], 16)
    # Key expansion k_0,(k_0)^' and k_1
    final_key = key_expansion(k)
    k_0, k_0dash, k_1 = final_key[0:16], final_key[16:32], final_key[32:48]
    
    # print_key(k_0, 'k_0')
    # print_key(k_0dash, 'k_0dash')
    # print_key(k_1, 'k_1')

    # initial state-key xor with k_0
    state = bitwise_xor(state, k_0)
    # core of the prince cipher
    state = core(state, k_1)
    # final state-key xor with k_0dash
    state = bitwise_xor(state, k_0dash)
    return list_to_hex(state)

def prince_decrypter(plaintext, key): #   alpha = c0ac29b7c97c50dd
    '''
    Decryption is same as encryption with slight tweak by alpha 
    '''
    final_key = "0000000000000000c0ac29b7c97c50dd"
    data = [0 for i in range(len(plaintext))]
    for i in range(len(plaintext)):
        data[i] = int(plaintext[i], 16)
    k = [0 for i in range(len(key))]
    for i in range(len(key)):
        k[i] = int(key[i], 16)
    final = [0 for i in range(len(final_key))]
    for i in range(len(final_key)):
        final[i] = int(final_key[i], 16)
    final = bitwise_xor(k, final)
    extended = key_expansion(final)
    k0prime = extended[0:16]
    k0 = extended[16:32]
    k1 = extended[32:48]
    data = bitwise_xor(data, k0)
    data = core(data, k1)
    data = bitwise_xor(data, k0prime)
    return list_to_hex(data)

# prince_encrypter("0123456789abcdef","0000000000000000fedcba9876543210")

#    plain_text           k_0            k_1           cipher_text
# 0000000000000000 00000000000000000000000000000000 818665aa0d02dfda
# ffffffffffffffff 00000000000000000000000000000000 604ae6ca03c20ada
# 0000000000000000 0000000000000000ffffffffffffffff 78a54cbe737bb7ef
# 0123456789abcdef 0000000000000000fedcba9876543210 ae25ad3ca8fa9ccf