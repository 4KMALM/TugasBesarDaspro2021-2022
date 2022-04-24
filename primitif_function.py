# ------- validasi input user -------
def validasi_input(masukan,role):
    perintah_user = ("list_game_toko","buy_game","list_game","search_my_game","search_game_at_store","riwayat","save","exit","help", "kerangajaib")
    perintah_admin = ("register","tambah_game","ubah_game","ubah_stok","list_game_toko","search_game_at_store","topup","save","exit","help", "kerangajaib")
    
    isAdmin = valid_item_in_arr(masukan,perintah_admin) 
    isUser = valid_item_in_arr(masukan,perintah_user)
    if masukan == "login":
        print("Anda sudah login.\nAnda harus keluar aplikasi terlebih dahulu dengan mengetik \"exit\"")
        return False
    else:
        if isAdmin or isUser:
            if role == "admin":
                if not(isAdmin):
                    print(f"Anda adalah admin. Hanya user yang dapat mengakses \"{masukan}\"")
                return isAdmin
            elif role == "user":
                if not(isUser):
                    print(f"Maaf, anda tidak memiliki izin untuk menjalankan perintah \"{masukan}\".\nMintalah ke administrator untuk melakukan hal tersebut.")
                return isUser
        else:
            print("Masukan anda tidak dikenali.\nKetik \"help\" untuk panduan penggunaan BINOMO")
            return False

# ---------- primitif lain -----------
def length(x): # implementasi len()
    count = 0
    for i in x:
        count += 1
    return count

def get_idx(lookFor,idx_lookFor,arr):
# jika tidak ketemu hasilnya -1
# jika ketemu hasilnya 0..N terdefinisi
# lookFor : hal yang dicari dapat apa saja
# idx_lookFor adalah indeks dalam list misal
    # "id" dalam arrGmae pasti berindeks 0
    # "nama" dalam arrGame pati berindeks 1
# arr adalah array of list yang akan dicari
    # array of list = [[list], N]; N: banyak terdefinisi (kecuali header)
    for i in range(1,arr[1]+1):
        if lookFor == arr[0][i][idx_lookFor]:
            return i
    else:
        return -1

def search_found(lookFor,idx_lookFor,arr):
# True jika ditemukan, dengan
# lookFor : hal yang dicari dapat apa saja
# idx_lookFor adalah indeks dalam list misal
    # "id" dalam arrGmae pasti berindeks 0
    # "nama" dalam arrGame pati berindeks 1
# arr adalah array of list yang akan dicari
    # array of list = [[list], N]; N: banyak terdefinisi (kecuali header)
    for i in range(0,arr[1]+1):
        if lookFor == arr[0][i][idx_lookFor]:
            return True
    else:
        return False

def get_thing_based(based,idx_based, arr,idx_lookfor):
# mengembalikan suatu variabel berdasarkan variabel unik (tidak sama dengan yang lain)
# misal : mengambil harga game berdasarkan id game
# based : data unik; idx_based : indek based dalam array
    # contoh : indeks id pada arrGame adalah 0
# idx_lookfor : indeks data yang ingin dicari
    for i in range(0,arr[1]+1):
        if based == arr[0][i][idx_based]:
            got = arr[0][i][idx_lookfor]
    return got

def valid_item_in_arr(item,arr):
    for i in arr:
        if item == i:
            return True
    else:
        return False

# ----- Fungsi/Prosedur selain modul -----

