from primitif_function import *


def last_game_id():
    game_data = data_constructor("game.csv")
    last_game_index = length(game_data)

    if last_game_index < 9:
        return "GAME00" + str(last_game_index+1)
    elif 9 <= last_game_index < 99:
        return "GAME0" + str(last_game_index+1)
    else:
        return "GAME" + str(last_game_index+1)


def tambah_game(x):
    salah = True
    while salah is True:
        q_list = ["nama game", "kategori", "tahun rilis", "harga", "stok awal"]
        new_game_data = [input("masukan " + i) for i in q_list]

        invalid = 0
        for tg_data in new_game_data:
            if tg_data == "":
                invalid += 1
            else:
                pass

        if invalid != 0:
            print("pesan error")
        else:
            x += [[last_game_id()] + new_game_data]
            print("jadi")
            salah = False
    return x


print(tambah_game(data_constructor("game.csv")))