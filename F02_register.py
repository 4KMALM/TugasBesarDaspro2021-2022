from primitif_function import *
import time 

"""
def gcd(a,b) :
    if (b==0):
        return a
    else:
        return gcd(b,a%b)

def coprime(b) :
    list = []
    a = 1 
    while a <= 75 :
        x = gcd(a,b)
        if x == 1 :
            list += [a]
        a += 1
    return list

def modInv(a,b) :
    c = 1 
    while  c <= b :
        x = (a*c)%b
        if x == 1 :
            return c
        else :
            pass
        c += 1

def ind(char) :
    kumpulan_elemen = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9','_'
                       'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
                       'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
def encrypt(password) :
    a = 73
    b = 20
    c = ""
    for i in password :
        x = ord(i) - ord("0")
        y = ((a*x + b)%75) + 48
        c += chr(y)
    return c

def decrypt(password) :
    a = 37
    b = 20
    c = ''
    for i in password :
        y = ord(i) - ord('0')
        x = a*(y-b)%75 + 48
        c += chr(x)
    return c
"""

def register(x) :
    nama = input("Masukkan nama anda : ")
    username = input("Masukkan username anda : ")
    password = input("Masukkan password anda : ")
    username_sama = True
    user_data = x[0]
    data_invalid = 0
    while username_sama :
        for data in user_data :
            if (username == data[1] or isInList(' ', username) or username == "") :
                data_invalid += 1
            else :
                pass
        if data_invalid != 0 :
            print("Username tidak tersedia silahkan gunakan username lain", end=" : ")
            username = input()
            data_invalid = 0
        else :
            print("Username tersedia!, silahkan menunggu proses")
            username_sama = False
    new_data = [ str(x[1]+1), username, nama, password,"user","0"]
    user_data += [new_data]
    x[1] += 1
    time.sleep(3)
    print()
    print("Pengguna berhasil ditambahkan!")
    return x
