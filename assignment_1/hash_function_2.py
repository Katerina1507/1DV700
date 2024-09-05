import random
import matplotlib.pyplot as plt

def get_hash_value(message):
    n = 0
    for c in message:
        n += ord(c)
    hash = n % 256
    return hash


def generation_word(length):
    word = ""
    for i in range(0, length):
        r = random.randint(ord("a"), ord("z"))
        word += chr(r)
    return word


def modifyBit(n, p):
    mask = 1 << p
    b = n & mask
    if b == 0:
        b = 1
    else:
        b = 0
    return (n & ~mask) | ((b << p) & mask)


def change_bit(s):
    pos = random.randint(0, len(s) - 1)
    code = ord(s[pos])
    code = modifyBit(code, random.randint(0, 7))
    c = chr(code)
    s = s[:pos] + c + s[pos+1:]
    return s


def main():
    dct1 = {}
    dct2 = {}
    for i in range(1000):
        len_word = random.randint(2, 50)
        word = generation_word(len_word)
        hash = get_hash_value(word)
        if hash in dct1:
            dct1[hash] += 1  # hash value
        else:
            dct1[hash] = 1
        word_change = change_bit(word)
        hash = get_hash_value(word_change)
        if hash in dct2:
            dct2[hash] += 1  # hash value
        else:
            dct2[hash] = 1
    #print(a)
    #print(b)
    b = sorted(dct1.items(), key=lambda x: x[0])
    xlist = [f[0] for f in b]
    ylist = [f[1] for f in b]
    plt.plot(xlist, ylist)
    b = sorted(dct2.items(), key=lambda x: x[0])
    xlist2 = [f[0] for f in b]
    ylist2 = [f[1] for f in b]
    plt.plot(xlist2, ylist2)
    plt.xlabel("Hash Values")
    plt.ylabel("Frequency")
    plt.title("Graph 2")
    plt.show()


# plt.plot(a.keys(),a.values())
# plt.title("Graph 2")
# plt.grid()
# plt.show()

main()