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
        for game in game_data :
            if game[0] in data_game :
                print("| {:<8}| {:<36}| {:<14}| {:<4}| {:<8}".format(game[0],game[1],game[2],game[3],game[4]))
            else :
                pass
