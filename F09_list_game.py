from primitif_function import *


def list_game(arrKepemilikan, arrGame, user_id) :
    data_game = []
    kepemilikan = arrKepemilikan[0]
    game_data = arrGame[0]
    for pemilik in kepemilikan :
        if user_id == pemilik[1] :
            data_game += [pemilik[0]]
    if length(data_game) == 0 :
        print("Maaf kamu belum membeli game, silahkan beli game terlebih dahulu")
    else :
        print("List yang game anda miliki : ")
        print("{:<4}| {:<8} | {:<36}| {:<14} | {:<5} | {:<8}".format('No','GAMEID','Nama Game','Kategori','Tahun','Harga'))
        n = 1
        for game in game_data :
            if isInList(game[0],data_game) :
                print("{:<4}| {:<8} | {:<36}| {:<14} | {:<5} | {:<8}".format(str(n),game[0],game[1],game[2],game[3],game[4]))
                n += 1
            else :
                pass
