from primitif_function import *

def riwayat(riwayat, user_id) :
    riwayat_user = []
    for data in riwayat :
        if data[3] == user_id :
            riwayat_user += [data]
    if length(riwayat_user) != 0 :
        print("Riwayat pembelian anda : ")
        for pembelian in riwayat_user :
            for i in range(5) :
                if i != 3 :
                    print(pembelian[i],end="|")
            print()
    else :
        print("Anda belum pernah melakukan pembelian")
        print("ketik \"buy_game\" untuk memulai pembalian")
