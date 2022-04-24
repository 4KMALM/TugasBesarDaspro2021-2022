# ------- fungsi load data ke list -------
def buat_tabData(data):
    # Buat struktur ([list],Neff)
    sum_line = 0
    with open(data, 'r') as f:
        for line in f:
            sum_line += 1

    # sum_line - 1 = 0 maka data kosong (hanya header)
    tabData = [[[] for i in range(sum_line)], sum_line-1]
    # mengakses tabData = ([listData],Neff)
    # tabData[0] -> akses listData; tabData[1] -> akses Neff
    nextline = '\n'; delimiter = ';'
    nLine = 0
    temp = ''
    with open(data, 'r') as f:
        for line in f:
            for char in line:
                if char == delimiter or char == nextline:
                    tabData[0][nLine] += [temp]
                    temp = ""
                else:
                    temp += char
            nLine += 1
        tabData[0][nLine-1] += [temp] # last temp
    return tabData 
# print(buat_tabData("game.csv"))
# [[['id', 'nama', 'kategori', 'tahun_rilis', 'harga', 'stock'], ['GAME001', 'Dying Light', '2015', 'Shoting', '250000', '10'], ['GAME002', 'White Shadows', '2016', 'Adventure', '215000', '15'], ['GAME003', 'BNMO - Play Along With Crypto', 'Adventure', '2022', '100000', '1'], ['GAME004', 'Dasar Pemrograman', 'Coding', '2021', '0', '10'], ['GAME005', 'Python Gemink', 'Coding', '1991', '69000', '999'], ['GAME006', 'Daspro Impact', 'Coding', '2018', '50000', '111']], 6]
# Ket: 1 : ada 1 data (selain judul)
# print(buat_tabData('Test1user.csv'))
# [[['id', 'username', 'nama', 'password', 'role', 'saldo'], ['1', 'username3', 'Kinanti Wening Asih', 'pass3', 'user', '10000000'], ['2', 'username4', 'Nadine Aliya Putri', 'pass4', 'user', '0']], 2]
# Ket: 2 : ada 2 data (selain judul)


# ---------- primitif lain -----------
def length(x): # implementasi len()
    count = 0
    for i in x:
        count += 1
    return count

def get_idx(lookFor,idx_lookFor,arr):
# jika tidak ketemu hasilnya -1
# jika ketemu return indeks 0..N terdefinisi
# lookFor : hal yang dicari dapat apa saja
# idx_lookFor adalah indeks dalam list misal
    # "id" dalam arrGmae pasti berindeks 0
    # "nama" dalam arrGame pati berindeks 1
# arr adalah array of list yang akan dicari
    # array of list = [[list], N]; N: banyak terdefinisi (kecuali header)
# misal : arr = [[["id1","dia"],["id2","aku"]],2]
# get_idx("id2",0, arr)
    # hasil -> 1 atau "id" ada di arr[0][1][0]
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
    for i in range(1,arr[1]+1):
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
    for i in range(1,arr[1]+1):
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
def validasi_input(masukan,role):
    perintah_user = ("list_game_toko","buy_game","list_game","search_my_game","search_game_at_store","riwayat","save","exit","help")
    perintah_admin = ("register","tambah_game","ubah_game","ubah_stok","list_game_toko","search_game_at_store","top_up","save","exit","help")
    
    isAdmin = valid_item_in_arr(masukan,perintah_admin) 
    isUser = valid_item_in_arr(masukan,perintah_user)
    if masukan == "login":
        print("Anda sudah login.\nAnda harus keluar aplikasi terlebih dahulu dengan mengetik \"exit\"")
        return False
    else:
        if isAdmin or isUser:
            if role == "admin":
                if not(isAdmin):
                    print(f"Maaf, anda tidak memiliki izin untuk menjalankan perintah \"{masukan}\".\nMintalah ke administrator untuk melakukan hal tersebut.")
                return isAdmin
            elif role == "user":
                if not(isUser):
                    print(f"Anda adalah admin. Hanya user yang dapat mengakses \"{masukan}\"")
                return isUser
        else:
            print("Masukan anda tidak dikenali.\nKetik \"help\" untuk panduan penggunaan BINOMO")
            return False
