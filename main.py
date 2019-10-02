from freq import show_freq
from decode import crack

def is_int(st):
    try:
        int(st)
        return True
    except:
        return False

if __name__ == "__main__":
    st = ""
    try:
        with open("st.txt", "r") as f:
            st = f.read().strip().lower()
    except:
        print("st.txt is not exist!")
        st = input("Enter Chipertext: ").strip().lower()

    show_freq(st, 20)

    while True:
        command = input("set key length, or press q to quit.\n")
        if command == "q":
            print("Bye~~")
            break
        elif is_int(command):
            crack(st, int(command))
        else:
            print("Not a number or command!")