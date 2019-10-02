def init_alpha_dic():
    alpha_dic = {}
    for i in range(ord('a'), ord('z')+1):
        alpha_dic.update({chr(i): 0})
    return alpha_dic


def alpha_freq(seq):
    I = 0
    seq_len = len(seq)
    seq = seq.lower()
    alpha_dic = init_alpha_dic()
    # print(alpha_dic)
    for ch in seq:
        alpha_dic[ch] += 1
    for i in range(ord('a'), ord('z')+1):
        alpha_num = alpha_dic[chr(i)]
        I += alpha_num * (alpha_num - 1)
    I = I / (seq_len * (seq_len - 1))
    return I


def split_st(st, sp):
    list1 = []
    if sp == 1:
        return st
    elif sp > 1:
        for i in range(0, sp):
            list1.append(st[i::sp])
        return list1
    else:
        print("Split Error!")
        return -1


def CI(st, sp):
    st_len = len(st)
    if sp == 1:
        I = alpha_freq(st)
        length = 0.027 * st_len / ((st_len - 1) * I - 0.038 * st_len + 0.065)
        print(f"Origial length: {length}")
        return I
    elif sp > 1:
        CI_list = []
        seqs = split_st(st, sp)
        for seq in seqs:
            CI_list.append(alpha_freq(seq))
        return sum(CI_list) / sp
    else:
        print("sp is error!")
        return -1

def show_freq(st, num=10):
    CI_list = []
    for i in range(1, num+1):
        ci = CI(st, i)
        CI_list.append((i, ci))
        print("{:02d}: {:.8f}".format(i, ci))
    print("-" * 50)
    print("top 10")
    c = 1
    CI_list.sort(key=lambda x: -x[1])
    for i, val in CI_list:
        if c == 10:
            break
        print("{:02d}: {:.8f}".format(i, val))
        c += 1
    return 0


if __name__ == "__main__":
    st = ""
    with open("st.txt", "r") as f:
        st = f.read().strip().lower()
    show_freq(st, 4)
