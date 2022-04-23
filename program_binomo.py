from primitif_function import *
from F15_load import load
from F03_login import login
from F14_help import help
import os

path_folder = load()

if path_folder != None:
    print("Selamat datang ")
    # Pembuatan memori
    arrGame = buat_tabData(os.path.join(path_folder, 'game.csv'))
    arrUser = buat_tabData(os.path.join(path_folder, 'user.csv'))
    arrRiwayat = buat_tabData(os.path.join(path_folder, 'riwayat.csv'))
    arrKepemilikan = buat_tabData(os.path.join(path_folder, 'kepemilikan.csv'))
    
    # Inisialisasi
    isLogin = False; exitGame = False; pengguna = ['id', 'username', 'nama', 'password', 'role', 'saldo']

    while not(exitGame): 
        user_input = input()

        if isLogin :
            if validasi_input(user_input, pengguna[4]) :
                if user_input == "register":
                    # register()
                    pass
                elif user_input == "tambah_game":
                    # tambah_game()z
                    pass
                elif user_input == "ubah_stock":
                    # ubah_stock()
                    pass
                elif user_input == "topup":
                    # topup
                    pass
                elif user_input == "buy_game":
                    # buy_game()
                    pass
                elif user_input == "list_game":
                    # list_game()
                    pass
                elif user_input == "search_my_game":
                    # search_my_game()
                    pass
                elif user_input == "riwayat":
                    # riwayat()
                    pass
                elif user_input == "list_game_toko":
                    # list_game_toko()
                    pass
                elif user_input == "search_game_at_store":
                    # search_game_at_store()
                    pass
                elif user_input == "save":
                    # save()
                    pass
                elif user_input == "exit":
                    # exit()
                    pass
                elif user_input == "help":
                    # help()
                    pass
        else:
            if user_input == "login":
                login(pengguna,arrUser,isLogin)
                isLogin = True
            else:
                help(isLogin,pengguna[4])
