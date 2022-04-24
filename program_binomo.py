import imp
from primitif_function import *
from F02_register import register
from F03_login import login
from F06_ubah_stock import ubah_stock
from F07_list_game_toko import list_game_toko
from F08_buy_game import buy_game
from F09_list_game import list_game
from F12_topup import topup
from F14_help import help
from F15_load import load
from F16_save import save
from F17_exit import exit

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
        user_input = input(">>> ")

        if isLogin :
            if validasi_input(user_input, pengguna[4]) :
                if user_input == "register":
                    arrUser = register(arrUser)

                elif user_input == "tambah_game":
                    # tambah_game()
                    # arrGame bertambah
                    pass

                elif user_input == "ubah_stock":
                    arrGame = ubah_stock(arrGame)

                elif user_input == "topup":
                    arrUser = topup(arrUser)

                elif user_input == "buy_game":
                    arrGame, arrUser, arrKepemilikan, arrRiwayat = buy_game(pengguna[0], arrGame, arrUser, arrKepemilikan, arrRiwayat)
                    # jika iduser belum punya game
                    # arrRiwayat bertambah
                    # arrKepemilikan bertambah
                    pass

                elif user_input == "list_game":
                    list_game(arrKepemilikan,arrGame,pengguna[0])
                
                elif user_input == "search_my_game":
                    # search_my_game()
                    # pakai arrKepemilikan dan arrGame
                    pass

                elif user_input == "riwayat":
                    # riwayat()
                    # pakai arrRiwayat 
                    pass

                elif user_input == "list_game_toko":
                    list_game_toko()

                elif user_input == "search_game_at_store":
                    # search_game_at_store()
                    # pakai arrGame
                    pass
            
                elif user_input == "save":
                    save()
                    # pakai semua array
                    pass

                elif user_input == "exit":
                    exit()
                    pass

                elif user_input == "help":
                    help()

        else:
            if user_input == "login":
                login(pengguna,arrUser,isLogin)
                isLogin = True
            else:
                help(isLogin,pengguna[4])
