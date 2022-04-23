from primitif_function import *

def topup(arrUser):
    usernm = input("Masukan username: ")
    plusSldo = int(input("Masukan saldo: "))
    found = search_found(usernm,1,arrUser)
    print()
    if found:
        cekSaldo = get_thing_based(usernm,1,arrUser,5)
        cekNama = get_thing_based(usernm,1,arrUser,2)
        totalSaldo = cekSaldo + plusSldo
        if totalSaldo >= 0 :
            print(f"Top up berhasil. Saldo {cekNama} bertambah menjadi {totalSaldo}")
        else:
            print(f"Masukan tidak valid")

    else:
        print(f"Username {usernm} tidak ditemukan")
