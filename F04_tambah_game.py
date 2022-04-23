from primitif_function import *


def last_game_id(arr):
    game_data = arr
    last_game_index = length(game_data)

    if last_game_index < 9:
        return "GAME00" + str(last_game_index+1)
    elif 9 <= last_game_index < 99:
        return "GAME0" + str(last_game_index+1)
    else:
        return "GAME" + str(last_game_index+1)


def tambah_game(arr):
    game_data = arr[0]
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

        try:
            for index in range(0, 4):
                if index == 3:
                    if int(new_game_data[3]) < 0:  # cek harga
                        invalid += 1
                    else:
                        pass
                elif index == 4:
                    if int(new_game_data[4]) < 0:  # cek stok awal
                        invalid += 1
                    else:
                        pass
        except ValueError:
            invalid += 1

        if invalid != 0:
            print("Masukan data dengan benar")
        else:
            game_data += [[last_game_id(data_constructor("game.csv"))] + new_game_data]
            arr[0] = game_data
            arr[1] = arr[1] + 1
            print("Game berhasil ditambahkan")
            salah = False
