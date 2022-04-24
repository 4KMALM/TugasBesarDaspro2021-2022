from primitif_function import *

def topup(arrUser):
    
# KAMUS LOKAL
# type user : <id, username, nama, password, role, saldo : string
#               >
# arrUser : array [1..N] of user
# usernm : string
# plusSldo, cekSaldo, totalSaldo : integer
# search_found : boolean
# nmUser : string

# ALGORITMA
    usernm = input("Masukan username: ")
    plusSldo = int(input("Masukan saldo: "))
    search_found = get_idx(usernm,1,arrUser) # Mengecek ada atau tidak username dalam array User
    
    print()
    if search_found: # Jika username ditemukan dalam array
        id_found = get_idx(usernm,1,arrUser) # Mencari indeks username
        cekSaldo = int(get_thing_based(usernm,1,arrUser,5)) # Mengecek saldo pengguna
        nmUser = get_thing_based(usernm,1,arrUser,2) # Mencari nama pengguna
        totalSaldo = cekSaldo + plusSldo
        if totalSaldo >= 0 :
            arrUser[0][id_found][5] = str(totalSaldo)
            print(f"Top up berhasil. Saldo {nmUser} bertambah menjadi {totalSaldo}")
        else:
            print(f"Masukan tidak valid")

    else:
        print(f"Username {usernm} tidak ditemukan")
    return(arrUser)
