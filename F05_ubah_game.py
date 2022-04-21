def FindGame(arrGame, ID):
# return indeks ditemukan game dalam array, jika tidak ditemukan, kembalikan -1

# KAMUS LOKAL
#   i : Int

# ALGORITMA
    i = 1   # data dimulai dari indeks 1
    while (i < arrGame[1]) and (arrGame[0][i][0] != ID):
        i = i + 1
    if (arrGame[0][i][0] != ID):
        i = -1
    return i

def UbahGame(arrGame):
# I.S. array daftar terdefinisi. F.S. elemen array daftar diperbarui berdasarkan masukan pengguna

# KAMUS LOKAL
#   ID : string
#   idx : Int
#   ulang : Char
#   nama, kategori, tahun, harga : string


# ALGORITMA
    ulang = 'Y' # inisialisasi
    idx = -1
    while (idx == -1) and (ulang == 'Y' or ulang == 'y'):   # ulangi hingga ID game terdapat dalam list, atau pengguna memilih untuk berhenti
        ID = input("Masukkan ID game: ")
        idx = FindGame(arrGame, ID) # cari indeks game dalam list

        if (idx == -1): # jika masukan ID tidak ditemukan, tampilkan pesan eror dan pilihan mengulang
            ulang = input("ID game tidak ditemukan, apakah anda ingin mengulang? (Y/N): ")
            while (ulang != 'Y' and ulang != 'y' and ulang != 'N' and ulang != 'n'):   # beri pesan kesalahan jika input tidak sesuai, dan ulang  hingga valid >:D
                ulang = input("Pilihan salah, ketik 'Y' atau 'N': ")
    
    # jika ID game sudah ditemukan, lanjutkan ke mengubah data
    if (ulang == 'y' or ulang == 'Y'):
        nama = input("Masukkan nama game: ")
        if (nama != ""):
            arrGame[0][idx][1] = nama

        kategori = input("Masukkan kategori: ")
        if (kategori != ""):
            arrGame[0][idx][2] = kategori

        tahun = input("Masukkan tahun rilis: ")
        if (tahun != ""):
            arrGame[0][idx][3] = int(tahun)

        harga = input("Masukkan harga: ")
        if (harga != ""):
            arrGame[0][idx][4] = int(harga)
        
    else:   # ID tidak ditemukan, dan pengguna memilih untuk tidak mengulang
        print("Mengubah data dibatalkan")
    
    return arrGame
