from operator import length_hint
from primitif_function import *

def search_game_at_store(arrGame):
# Menerima masukan data game dari user lalu mencari data tersebut dalam toko dan menuliskan hasil yang sesuai
# I.S arrGame terdefinisi
# F.S. menuliskan ke layar game-game sesuai masukan user

# KAMUS LOKAL
# constant
    # selection_q = list
# Variabel
    # temp_data, selection_list = list
    # data_lenght = int
# ALGORITMA
    temp_data = arrGame[0]  # Parsed CSV
    data_length = arrGame[1]  # Neff (Length parsed csv)

    if arrGame[1] == 0: # Penanganan kasus
        print("Mohon maaf daftar game sedang tidak tersedia")
    else:
        selection_q = ["ID", "Nama", "Kategori", "Tahun Rilis", "Harga"]  # selection question
        selection_list = [input("Masukan " + i + " Game : ") for i in selection_q]  # selection list

        if data_length-1 == 0:
            print("Tidak ada game yang cocok")
        else:
            print("{:<4}|{:^9}|{:^36}|{:^16}|{:^13}|{:^11}|{:^6}|".format("No","ID Game","Nama Game","Kategori","Tahun Rilis","Harga","stok"))
            print("-"*102)
            j = 0

            for i in range(1,data_length+1):
                if (selection_list[0] == temp_data[i][0] or selection_list[0] == "") and (selection_list[1] == temp_data[i][1] or selection_list[1] == "") and (selection_list[2] == temp_data[i][2] or selection_list[2] == "") and (selection_list[3] == temp_data[i][3] or selection_list[3] == "") and (selection_list[4] == temp_data[i][4] or selection_list[4] == ""):
                    print("{:<4}|{:<9}|{:<36}|{:<16}|{:<13}|{:<11}|{:<6}|".format(f"{i}.",temp_data[i][0],temp_data[i][1],temp_data[i][2],temp_data[i][3],temp_data[i][4],temp_data[i][5]))



