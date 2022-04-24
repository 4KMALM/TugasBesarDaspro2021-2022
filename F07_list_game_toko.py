from primitif_function import *

def checking(argument, arr):
    val = False
    for i in arr:
        if i == argument:
            val = True
            return val
        else:
            pass
    return val


def list_of_option(data, param):  # looking for option
    list_ = []
    if param == "Tahun" or param == "tahun":
        for i in range(1, length(data)):
            if checking(data[i][3], list_) is True:
                pass
            else:
                list_ += [int(data[i][3])]
    elif param == "Harga" or param == "harga":
        for i in range(1, length(data)):
            if checking(data[i][4], list_) is True:
                pass
            else:
                list_ += [int(data[i][4])]
    return list_


def arranging_(arr, ad):  # arranging option
    awal = 0
    if ad == "+":
        for i in range(length(arr)):
            for j in range(awal, length(arr)):
                if arr[i] > arr[j]:
                    temp = arr[j]
                    arr[j] = arr[i]
                    arr[i] = temp
            awal += 1
    elif ad == "-":
        for i in range(length(arr)):
            for j in range(awal, length(arr)):
                if arr[i] < arr[j]:
                    temp = arr[j]
                    arr[j] = arr[i]
                    arr[i] = temp
            awal += 1
    return arr


def sorted_data(list_baru, data, param):  # sorting data
    length_data = length(data)
    new_data = []
    if param == "Tahun" or param == "tahun":
        for isi in list_baru:
            for i in range(1, length_data):
                if data[i][3] == str(isi):
                    if data[i] in new_data:
                        pass
                    else:
                        new_data += [data[i]]
    elif param == "Harga" or param == "harga":
        for isi in list_baru:
            for i in range(1, length_data):
                if data[i][4] == str(isi):
                    if data[i] in new_data:
                        pass
                    else:
                        new_data += [data[i]]
    return new_data


def outputing_(arr):  # output
    for i in range(length(arr)):
        for j in range(6):
            if j != 5:
                print(arr[i][j], end=" | ")
            else:
                print(arr[i][j])


def list_game_toko(arr_of_arr):
    game_data = arr_of_arr[0]
    list_skema = ["Tahun", "Harga", "tahun", "harga"]
    list_ad = ["+", "-"]
    skema = input("Skema sorting: ")

    if length(skema) > 2:
        length_scheme = length(skema)
        sort_scheme = skema[0:length_scheme-1]
        cond_ad = skema[length_scheme-1]
    else:
        sort_scheme = ""
        cond_ad = ""

    if checking(sort_scheme, list_skema) and checking(cond_ad, list_ad):
        list_baru = arranging_(list_of_option(game_data, sort_scheme), cond_ad)
        new_sorted_data = sorted_data(list_baru, game_data, sort_scheme)
        outputing_(new_sorted_data)
    elif skema == "":
        outputing_(game_data)
    else:
        print("masukan tidak valid")

# ----cek-----
# print(list_game_toko([[['id', 'nama', 'kategori', 'tahun_rilis', 'harga', 'stock'], ['GAME001', 'Dying Light', 'Shoting', '2015', '250000', '10'], ['GAME002', 'White Shadows', 'Adventure', '2016', '215000', '15'], ['GAME003', 'BNMO - Play Along With Crypto', 'Adventure', '2022', '100000', '1'], ['GAME004', 'Dasar Pemrograman', 'Coding', '2021', '0', '10'], ['GAME005', 'Python Gemink', 'Coding', '1991', '69000', '999'], ['GAME006', 'Daspro Impact', 'Coding', '2018', '50000', '111']], 6]))
