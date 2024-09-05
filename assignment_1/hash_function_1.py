import random
import matplotlib.pyplot as plt
# import math


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


def main():
    # res=generation_word(10)
    # print(res)
    a = {}
    for i in range(1000):
        len_word = random.randint(2,50)
        word = generation_word(len_word)
        hash = get_hash_value(word)
        if hash in a:
            a[hash] += 1  # hash value
        else:
            a[hash] = 1
    print(a)

    b = sorted(a.items(), key=lambda x: x[0])
    xlist = [f[0] for f in b]
    ylist = [f[1] for f in b]
    plt.plot(xlist, ylist)
    plt.xlabel("Hash Values")
    plt.ylabel("Frequency")
    plt.title("Graph 1")  
    plt.grid()
    plt.show()
    # plt.plot(a.keys(),a.values())
    # plt.title("Graph") 
    # plt.grid()
    # plt.show()

main()