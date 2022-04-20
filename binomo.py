# Kamus
log = False
command = False
perintah_user = ("list_game_toko","beli_game","list_game_saya","cari_game_saya","cari_game_toko","riwayat","help")
perintah_admin = ("registrasi","tambah_game","ubah_game","ubah_stok","list_game_toko","cari_game_toko","top_up")
perintah_valid =  tuple

# Main Algorithm Binomo
# langsung disuruh login
print("Selamat datang di BINOMO")
print("Sebelum memulai silahkan login terlebih dahulu")
username = input("masukkan username anda : ")
password = input("masukkan password anda : ")
log = login(username,password)
identitas = identitas(username,password)

# Looping validation login
# kalau masukan selain login bakal looping terus sampai valid
# sekaligus ngisi data pemakai (role, nama) biar bisa interaktif
# sekaligus mastiin command yang ada cuman buat user or admin
while not(log) :
    print("masukkan anda salah silahkan ulangi lagi")
    username = input("masukkan username anda : ")
    password = input("masukkan password anda : ")
    log = login(username,password)
if log :
    nama = identitas[2]
    role = identitas[4]
    print("selamat datang" + nama + "! Selamat datang di BINOMO")
    command = True
    if role == "Admin" :
        perintah_valid = perintah_admin
    elif role == "User" :
        perintah_valid = perintah_user

# looping command sampai ada perintah exit
while command : 
    print("silahkan masukkan perintah anda")
    print("untuk membuka daftar perintah ketik \"help\"")
    perintah = input()

    
