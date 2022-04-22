from primitif_function import *


def ubah_stock(arrGame):
    id_game = input()
    id_found = search_found(id_game,0,arrGame)
    if id_found:
        name_game = get_thing_based(id_game,0,arrGame,1)
        init_stock = get_thing_based(id_game,0,arrGame,5)
        stock_in = int(input())
        if init_stock+stock_in < 0 :
            print(f"Stok game {name_game} gagal dikurangi karena stok kurang. Stok sekarang: {init_stock} (< {abs(stock_in)})")
        else:
            fnl_stock = init_stock + stock_in
            print(f"Stok game {name_game} berhasil dikurangi. Stok sekarang: {fnl_stock}")
    else:
        print("Tidak ada game dengan ID tersebut!")
