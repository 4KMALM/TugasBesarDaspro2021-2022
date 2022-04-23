from primitif_function import *


def search_game_at_store(arrGame):  # input(
    temp_data = arrGame[0]  # Parsed CSV
    data_length = arrGame[1]  # Neff (Length parsed csv)

    selection_q = ["ID", "Nama", "Kategori", "Tahun Rilis", "Harga"]  # selection question
    selection_list = [input("Masukan " + i + " Game :") for i in selection_q]  # selection list

    indx = 0  # index

    # game selection from selection_list
    for i in range(5):
        if selection_list[i] == "":
            indx += 1
            pass
        else:
            game_data = []
            for j in range(data_length):
                if temp_data[j][indx] == selection_list[i]:
                    game_data += [temp_data[j]]
            temp_data = game_data
            indx += 1

    # output from filtered game
    if length(temp_data) == 0:
        print("Tidak ada game yang cocok")
    else:
        for i in range(1, length(temp_data)):
            for j in range(6):
                if j != 5:
                    print(temp_data[i][j], end=" | ")
                else:
                    print(temp_data[i][j])
