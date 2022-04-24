import os
from primitif_function import *


# how to use
# input parameter :
# in sequence (kalau ketuker nanti isi filenya beda)
# nama folder
# array game
# array user
# array riwayat
# array kepemilikan

# digunakan khusus saving 4 file eksternal
def save(arrGame, arrUser, arrRiwayat, arrKepemilikan) :
    namafolder = input("Masukkan nama folder penyimpanan: ")
    # Kamus Lokal
    # Array File : Array of tuple (TabData, SeqFile of Tab Data)
    # TabData 
    # namafile : string namafile (by default, nama.csv)
    # namafolder : string directory
    # Array
    ArrayFile = [(arrGame,'game.csv'),(arrUser,'user.csv'),(arrRiwayat,'riwayat.csv'),(arrKepemilikan,'kepemilikan.csv')]
    list_dir = os.listdir(os.getcwd())
    if isInList(namafolder,list_dir) :
        os.chdir(namafolder)
        for file in ArrayFile :
            TabData = file[0]
            namafile = file[1]
            Array = TabData[0]
            f = open(namafile,'w')
            for i in range(length(Array)) :
                intro = ''
                panjang = length(Array[i])
                for indeks in range(panjang) :
                    if indeks == panjang-1 :
                        intro += str(Array[i][indeks]) + '\n'
                    else :
                        intro += str(Array[i][indeks]) + ';'
                f.write(intro)
            f.close()
    else :
        os.mkdir(namafolder)
        os.chdir(namafolder)
        for file in ArrayFile :
            TabData = file[0]
            namafile = file[1]
            Array = TabData[0]
            f = open(namafile,'x')
            for i in range(length(Array)) :
                intro = ''
                panjang = length(Array[i])
                for indeks in range(panjang) :
                    if indeks == panjang-1 :
                        intro += str(Array[i][indeks]) + '\n'
                    else :
                        intro += str(Array[i][indeks]) + ';'
                f.write(intro)
            f.close()
    print("Data berhasil tersimpan.")
"""
check = input()
arrGame = [[['id,nama,kategori,tahun_rilis,harga,stock'], ['GAME001,Dying Light,2015,Shoting,250000,10'], ['GAME002,White Shadows,2016,Adventure,215000,15'], ['GAME003,BNMO - Play Along With Crypto,Adventure,2022,100000,1'], ['GAME004,Dasar Pemrograman,Coding,2021,0,10'], ['GAME005,Python Gemink,Coding,1991,69000,999'], ['GAME006,Daspro Impact,Coding,2018,50000,111', '']], 6]
arrUser = [[['id', 'username', 'nama', 'password', 'role', 'saldo'], ['1', 'fabian_si_banyak_fansnya00', 'Fabian Savero', 'yukmainbinomo', 'user', '100000'], ['2', 'akmal_ma', 'Akmal', 'akumaru', 'admin', '0'], ['3', 'username1', 'Zakariyya Gambetta', 'pass1', 'admin', '0'], ['4', 'username2', 'Margaretha Olivia', 'pass2', 'admin', '0'], ['5', 'username3', 'Kinanti Wening Asih', 'pass3', 'user', '10000000'], ['6', 'username4', 'Nadine Aliya Putri', 'pass4', 'user', '0']], 6] 
arrRiwayat = [[['game_id', 'nama', 'harga', 'user_id', 'tahun_beli'], ['GAME001', 'Dying Light', '250000', '1', '2022'], ['GAME002', 'White Shadows', '215000', '1', '2022'], ['GAME003', 'BNMO - Play Along With Crypto', '100000', '3', '2020']], 3]
arrKepemilikan = [[['game_id', 'user_id'], ['GAME001', '1'], ['GAME002', '2'], ['GAME003', '2'], ['GAME001', '3'], ['GAME004', '1'], ['GAME005', '1']], 6]
      
save(check,arrGame,arrUser,arrRiwayat,arrKepemilikan)
"""
