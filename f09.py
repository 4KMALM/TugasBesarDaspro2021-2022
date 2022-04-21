from primitif_function import *


def list_game(kepemilikan, game_data, user_id) :
    data_game = []
    for pemilik in kepemilikan :
        if user_id == pemilik[1] :
            data_game += [pemilik[0]]
    if length(data_game) == 0 :
        print("Maaf kamu membeli game, silahkan beli game terlebih dahulu")
    else :
        for game in game_data :
            if game[0] in data_game :
                for i in range(5) :
                    print(game[i],end="|")
                print()

