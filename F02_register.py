from primitif_function import *
import time 

def encrypt(password) :
    a = 12345
    b = 3334
    c = ""
    for i in password :
        x = ord(i) - ord("0")
        y = ((a*x + b)%75) + 48
        c += chr(y)
    return c

def decrypt(password) :
    pass

def register(x,nama,username,password) :
    username_sama = True
    user_data = x[0]
    data_invalid = 0
    while username_sama :
        for data in user_data :
            if username == data[1] :
                data_invalid += 1
            else :
                pass
        if data_invalid != 0 :
            print("Username tidak tersedia silahkan masukkan username yang lain", end=" : ")
            username = input()
            data_invalid = 0
        else :
            print("Username tersedia!, silahkan menunggu proses")
            username_sama = False
    new_data = [ str(x[1]+1), username, nama, password,"User","0"]
    user_data += [new_data]
    x[1] += 1
    time.sleep(3)
    print()
    print("Pengguna berhasil ditambahkan!")
    return x
