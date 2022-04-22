# ------- fungsi membuat list dari file -------
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
# [[['id', 'nama', 'kategori', 'tahun_rilis', 'harga', 'stock'], ['GAME001', 'Dying Light', '2015', 'Shoting', '250000', '10']], 1]
# Ket: 1 : ada 1 data (selain judul)
# print(buat_tabData('user.csv'))
# [[['id', 'username', 'nama', 'password', 'role', 'saldo'], ['1', 'username3', 'Kinanti Wening Asih', 'pass3', 'user', '10000000'], ['2', 'username4', 'Nadine Aliya Putri', 'pass4', 'user', '0']], 2]
# Ket: 2 : ada 2 data (selain judul)


# ---------- primitif lain -----------
def length(x): # implementasi len()
    count = 0
    for i in x:
        count += 1
    return count

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
