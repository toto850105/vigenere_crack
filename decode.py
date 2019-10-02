letter_list = list("abcdefghijklmnopqrstuvwxyz")
freq_list = [0.08167, 0.01492, 0.02782, 0.04253, 0.12702, 0.02228, 0.02015, 0.06094, 0.06966, 0.00153, 0.00772, 0.04025,
             0.02406, 0.06749, 0.07507, 0.01929, 0.00095, 0.05987, 0.06327, 0.09056, 0.02758, 0.00978, 0.0236, 0.0015, 0.01974, 0.00074]


def shift(l, n):
    return tuple(l[n:] + l[:n])


def crack(text, sp):
    if sp == 1:
        print("sp is 1!!")
        return -1
    elif sp < 1:
        print("Error sp value!")
        return -1
    st_list = []
    keys = []
    for i in range(0, sp):
        st_list.append(list(text[i::sp]))
    for i in range(0, sp):
        W, J = [], []
        I = 25
        t = 0
        for charc in letter_list:
            W.append(round((st_list[i].count(charc) / 26), 8))
        while I > 0:
            num = 0
            for (a, b) in zip(W, shift(freq_list, t)):
                num += (a * b)
            J.append(round(num, 8))
            I -= 1
            t += 1
        F = [D for D, E in enumerate(J) if E == max(J)]
        F[0] = ((26 - F[0]) % 26)
        key = chr(ord('a') + F[0])
        keys.append(key)
        # S1, S2 = [], []
        # for char in st_list[i]:
        #     S1.append(((ord(char) - 97) - F[0]) % 26)
        # for id2 in S1:
        #     S2.append(id2 - ord('a'))
        # st_list[i] = S2
    print(f"key length: {sp}")
    print("key is: {}".format(''.join(keys)))
    print("plaintext is :")
    decode(text, ''.join(keys))
    print()
    return 0


def decode(ciphertext, key):
    plaintext = ''
    key_len = len(key)
    key_int = [ord(i) for i in key]
    ciphertext_int = [ord(i) for i in ciphertext]
    for i in range(len(ciphertext_int)):
        v = (ciphertext_int[i] - key_int[i % key_len]) % 26
        plaintext = "".join([plaintext, chr(v+65)])
    print(plaintext)
    return plaintext



if __name__ == "__main__":
    st = ""
    with open("st.txt", "r") as f:
        st = f.read().strip().lower()
    crack(st, 4)
