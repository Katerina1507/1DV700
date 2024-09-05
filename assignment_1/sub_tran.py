import math

def encrypt_substituon(text, s):
    result = ""
    for i in range(len(text)):
        char = text[i]
        if char.isalpha():
            if (char.isupper()):
                result += chr((ord(char) + s-65) % 26 + 65)
            else:
                result += chr((ord(char) + s - 97) % 26 + 97)
        else:
            result += char
    return result

def decrypt_substituion(text, s):
    result = ""
    for i in range(len(text)):
        char = text[i]
        if char.isalpha():
            if (char.isupper()):
                result += chr((ord(char) - s-65) % 26 + 65)
            else:
                result += chr((ord(char) - s - 97) % 26 + 97)
        else:
            result += char
    return result


def encrypt_transposition(text, key):
    cipher = ""
    k_indx = 0
    text_lst = list(text)
    key_lst = sorted(list(key))
    column = len(key)

    row = int(math.ceil(len(text) / column))
    fill_null = row * column - len(text)
    text_lst.extend('_' * fill_null)
    matrix = [text_lst[i: i + column] for i in range(0, len(text_lst), column)]
    for _ in range(column):
        curr_idx = key.index(key_lst[k_indx])
        cipher += ''.join([row[curr_idx] for row in matrix])
        k_indx += 1

    return cipher

def decrypt_transposition(cipher, key):
    msg = ""
    k_indx = 0
    msg_indx = 0
    msg_lst = list(cipher)
    col = len(key)

    row = int(math.ceil(len(cipher) / col))
    key_lst = sorted(list(key))
    dec_cipher = []
    for _ in range(row):
        dec_cipher += [[None] * col]
    for _ in range(col):
        curr_idx = key.index(key_lst[k_indx])
        for j in range(row):
            dec_cipher[j][curr_idx] = msg_lst[msg_indx]
            msg_indx += 1
        k_indx += 1
    try:
        msg = ''.join(sum(dec_cipher, []))
    except TypeError:
        raise TypeError("This program cannot", "handle repeating words.")

    null_count = msg.count('_')

    if null_count > 0:
        return msg[: -null_count]

    return msg




def main():
    
    ws = input("Enter S if you want to make substituon method and T if you want to make transposition: ")
    sz = input("Enter E if you want to make Encryption and D if you want to make decryption:  ")
    ks = input("Enter H if you want to write a text or U if you want to upload a text: ")

    if ks == "H":
        text = input("enter a text:  ")
    else:
        filename = input("Enter a file name:")
        file = open(filename)
        text = file.read()
        file.close()

    if ws == "S":
        key = int(input("Enter a key: "))
        if sz == "E":
            result = encrypt_substituon(text, key)
        else:
            result = decrypt_substituion (text,key)
    else:
        key = input("Enter a key: ")
        if sz == "E":
            result = encrypt_transposition(text, key)
        else:
            result = decrypt_transposition(text, key)  
    print(result)
    
main()


