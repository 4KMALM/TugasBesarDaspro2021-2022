from primitif_function import *


def search_game_at_store():
    temp_data = data_constructor("game.csv")

    selection_q = ["ID", "Nama", "Kategori", "Tahun Rilis", "Harga"]
    selection_list = [input("Masukan " + i + " Game :") for i in selection_q]

    indx = 0

    for q in selection_list:
        if q == "":
            indx += 1
            pass
        else:
            game_data = [["", "", "", "", ""]]
            for game_line in temp_data:
                if game_line[indx] == q:
                    game_data += [game_line]
            temp_data = game_data
            indx += 1

    if length(temp_data) == 1:
        pass
    else:
        for i in range(1, length(temp_data)):
            print(temp_data[i])


search_game_at_store()