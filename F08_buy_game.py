from primitif_function import *
import datetime

def buy_game(user_id, arrGame, arrUser, arrKepemilikan, arrRiwayat):
# KAMUS LOKAL
# type user : <id, username, nama, password, role, saldo : string
#               >
# type game : < id_game, nama game, kategori, tahun rilis, harga, stok awal : string
#               >
# type kepemilikan : < id_game, id : string
#                      >
# type riwayat : < id_game, nama, harga, id, tahun rilis : string
#                  >
# arrUser : array [1..N] of user
# arrGame : array [1..N] of game
# arrKepemilikan : array [1..N] of kepemilikan
# arrRiwayat : array [1..N] of riwaya
# user_id, id_game : string
# idx_game, idx_user : integer
# found = boolean
# cekSldo, cekHrgaGm, cekStok : integer
# nmGame,thnRilis : string

# ALGORITMA
    id_game = input("Masukkan ID Game: ")

    if not(search_found(id_game,0,arrGame)): # cek apakah id game tidak ada
        print("Tidak ada game dengan id tersebut")

    else: # id_game tersedia di toko
        # list game yang dimiliki user
        gameUser = [[],0]
        for i in range(arrKepemilikan[1]):
            if arrKepemilikan[0][i][1] == user_id:
                gameUser[0] += [[arrKepemilikan[0][i][0]]]
                gameUser[1] += 1
        gameUser[1] -= 1
    
        gameFound = search_found(id_game,0,gameUser)
        
        if not(gameFound):
            print("Anda sudah memiliki Game tersebut!")

        else: # user belum memiliki game
            # Cek saldo yang dimiliki user
            cekSldo = int(get_thing_based(user_id,0,arrUser,5))
            # Cek harga game yang akan dibeli
            cekHrgaGm = int(get_thing_based(id_game,0,arrGame,4))

            if cekSldo < cekHrgaGm:
                print("Saldo anda tidak cukup untuk membeli Game tersebut!")
            else:
                # Cek stok game di toko
                cekStok = int(get_thing_based(id_game,0,arrGame,5))
                if cekStok == 0:
                    print("Stok Game tersebut sedang habis")
                else: # cekStock > 0
                    idx_game = get_idx(id_game,0,arrGame) # indeks game yang dibeli
                    idx_user = get_idx(user_id,0,arrUser) # indeks user

                    # Cek nama game yang akan dibeli
                    nmGame = get_thing_based(id_game,0,arrGame,1)
                    # Tahun beli game
                    year_now = str(datetime.datetime.now().year)

                    arrUser[0][idx_user][5] = str(cekSldo - cekHrgaGm) # Mengganti data saldo pada array User
                    arrGame[0][idx_game][5] = str(cekStok-1) # Mengganti jumlah stok pada array Game

                    arrKepemilikan[0] += [[id_game,user_id]] # Menambah game ke daftar kepemilikan user
                    arrRiwayat[0] += [[id_game, nmGame, cekHrgaGm, user_id, year_now]]
                    print(f"Game {nmGame} berhasil dibeli")
    return(arrGame, arrUser, arrKepemilikan, arrRiwayat)
