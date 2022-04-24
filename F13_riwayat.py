from primitif_function import *

def riwayat(arrRiwayat, user_id) :
    riwayat = arrRiwayat[0]
    riwayat_user = []
    for data in riwayat :
        if data[3] == user_id :
            riwayat_user += [data]
    if length(riwayat_user) != 0 :
        print("Riwayat pembelian anda : ")
        print("{:<4}|{:<8}|{:<36}|{:<8}|{:<10}".format('No','GAMEID','Nama Game','Harga','Tahun Beli'))
        n = 1
        for pembelian in riwayat_user :
                    print("{:<4}|{:<8}|{:<36}|{:<8}|{:<10}".format(str(n),pembelian[0],pembelian[1],pembelian[2],pembelian[4]))
                    n += 1
    else :
        print("Anda belum pernah melakukan pembelian")
        print("ketik \"buy_game\" untuk memulai pembalian")
