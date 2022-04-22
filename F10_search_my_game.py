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

def SearchInven(arrGame, arrMilik, userID):
# I.S. array daftar terdefinisi. F.S. menuliskan ke layar game pada inventory yang memenuhi kriteria pencarian

# KAMUS LOKAL
# gameUser : <array of Int; Int>
# ID : string
# tahun : Int
# i, idx, n : Int

# ALGORITMA
    gameUser = [[0 for _ in range(arrMilik[1]+1)], 0]   # inisialisasi array daftar game yang dimiliki pengguna
    
    for i in range(1, arrMilik[1]+1):
        if (arrMilik[0][i][1] == userID):
            gameUser[1] = gameUser[1] + 1
            gameUser[0][gameUser[1]] = FindGame(arrGame, arrMilik[0][i][0])
        
        
    if (gameUser[1] == 0):
        print("Maaf, kamu belum membeli game. Ketik perintah beli_game untuk beli.")
    
    else:
        ID = input("Masukkan ID Game: ")
        tahun = input("Masukkan Tahun Rilis Game: ")

        n = 0
        print("\nDaftar game pada inventory yang memenuhi kriteria:")
        for i in range(1,gameUser[1]+1):
            idx = gameUser[0][i]
            if (ID == "" or ID == arrGame[0][idx][0]) and (tahun == "" or tahun == str(arrGame[0][idx][2])):
                n = n + 1
                print('{:<4} {:^8} | {:^36} | {:^10} | {:^10} | {:^4}'.format((str(n)+'.'),arrGame[0][idx][0],arrGame[0][idx][1],str(arrGame[0][idx][4]),arrGame[0][idx][2],str(arrGame[0][idx][3])))
            
        
        if (n == 0):
            print("Tidak ada game pada inventory yang memenuhi kriteria")