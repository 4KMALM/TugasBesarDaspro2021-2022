from primitif_function import *

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
    id_game = input("Masukan ID Game: ")

    kepemilikan = [id_game,id,'','','','']

    found = search_found(id_game,0,arrKepemilikan) # cek apakah game sudah dimiliki user atau belum
    idx_game = get_idx(id_game,0,arrGame) # indeks game yang dibeli
    idx_user = get_idx(id_game,0,arrUser) # indeks user
    
    if found: # id Game ditemukan dalam kepemilikan user
        print("Anda sudah memiliki Game tersebut!")

    else: # user belum memiliki game
        # Cek saldo yang dimiliki user
        cekSldo = int(get_thing_based(id,0,arrUser,5))
        # Cek harga game yang akan dibeli
        cekHrgaGm = int(get_thing_based(id_game,0,arrGame,4))
        # Cek nama game yang akan dibeli
        nmGame = get_thing_based(id_game,0,arrGame,1)
        # Cek tahun rilis game yang akan dibeli
        thnRilis = get_thing_based(id_game,0,arrGame,3)

        if cekSldo >= cekHrgaGm: # Jika saldo pengguna cukup untuk membeli game
            # Cek stok game di toko
            cekStok = int(get_thing_based(id_game,0,arrGame,5))
            if cekStok > 0 : # Stok tersedia di toko
                arrUser[0][idx_user][5] = str(cekSldo - cekHrgaGm) # Mengganti data saldo pada array User
                arrGame[0][idx_game][5] = str(cekStok-1) # Mengganti jumlah stok pada array Game
                arrKepemilikan += [kepemilikan] # Menambah game ke daftar kepemilikan user
                arrRiwayat += [[id_game, nmGame, cekHrgaGm, id, thnRilis ]] # Menambah riwayat pembelian game
                print(f"Game {nmGame} berhasil dibeli")
            elif cekStok == 0 : # stok game = 0
                print("Stok Game tersebut sedang habis")

        else: # Saldo pengguna tidak cukup untuk membeli game
            print("Saldo anda tidak cukup untuk membeli Game tersebut!")
    return(arrGame, arrUser, arrKepemilikan, arrRiwayat)


        



