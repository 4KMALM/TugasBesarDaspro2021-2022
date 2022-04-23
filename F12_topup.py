from primitif_function import *

def topup(arrUser):
    usernm = input("Masukan username: ")
    plusSldo = int(input("Masukan saldo: "))
    search_found = get_idx(usernm,1,arrUser)
    print()
    if search_found:
        id_found = get_idx(usernm,1,arrUser)
        cekSaldo = int(get_thing_based(usernm,1,arrUser,5))
        cekNama = get_thing_based(usernm,1,arrUser,2)
        totalSaldo = cekSaldo + plusSldo
        if totalSaldo >= 0 :
            arrUser[0][id_found][5] = totalSaldo
            print(f"Top up berhasil. Saldo {cekNama} bertambah menjadi {totalSaldo}")
        else:
            print(f"Masukan tidak valid")

    else:
        print(f"Username {usernm} tidak ditemukan")
    return(arrUser)
