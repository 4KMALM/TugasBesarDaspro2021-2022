import argparse
import os

# ------- Prosedur load() -------
def load():
# Input : -
# output : 
# JIka nama folder ada : sebuah path folder, dengan folder pasti berisi file yang akan digunakan
# JIka tidak dikembalikan sebuah None type

    parser = argparse.ArgumentParser()  
    parser.add_argument("folder", type = str, nargs="?")    # Menerima masukan string (tanpa spce) ketika program dijalankan
    args = parser.parse_args()

    if args.folder != None: # JIka args diberikan suatu nilai
        for dirpath, dirnames, filenames in os.walk(os.getcwd()):   # pencarian nama folder
            for dir in dirnames:
                if dir == args.folder:
                    break

            if dir == args.folder:
                return os.path.join(dirpath,args.folder)
                break
        else: 
            print(f"Folder \"{args.folder}\" tidak ditemukan.")
    else: # Jika args empty string
        print("Tidak ada nama folder yang diberikan!")

# REALISASI
# $ python F15-load.py nama_folder
# ouput; print(load())
# Disk:/..pathfolder../nama_folder

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

# KEPERLUAN TESTER
# print(buat_tabData("game.csv"))
# [[['id', 'nama', 'kategori', 'tahun_rilis', 'harga', 'stock'], ['GAME001', 'Dying Light', 'Shoting', '2015', '250000', '10'], ['GAME002', 'White Shadows', 'Adventure', '2016', '215000', '15'], ['GAME003', 'BNMO - Play Along With Crypto', 'Adventure', '2022', '100000', '1'], ['GAME004', 'Dasar Pemrograman', 'Coding', '2021', '0', '10'], ['GAME005', 'Python Gemink', 'Coding', '1991', '69000', '999'], ['GAME006', 'Daspro Impact', 'Coding', '2018', '50000', '111']], 6]
# Ket: 1 : ada 1 data (selain judul)
# print(buat_tabData('user.csv'))
# [[['id', 'username', 'nama', 'password', 'role', 'saldo'], ['1', 'fabian_si_banyak_fansnya00', 'Fabian Savero', 'yukmainbinomo', 'user', '100000'], ['2', 'akmal_ma', 'Akmal', 'akumaru', 'admin', '0'], ['3', 'username1', 'Zakariyya Gambetta', 'pass1', 'admin', '0'], ['4', 'username2', 'Margaretha Olivia', 'pass2', 'admin', '0'], ['5', 'username3', 'Kinanti Wening Asih', 'pass3', 'user', '10000000'], ['6', 'username4', 'Nadine Aliya Putri', 'pass4', 'user', '0']], 6]
# Ket: 2 : ada 2 data (selain judul)
# print(buat_tabData('riwayat.csv'))
# [[['game_id', 'nama', 'harga', 'user_id', 'tahun_beli'], ['GAME001', 'Dying Light', '250000', '1', '2022'], ['GAME002', 'White Shadows', '215000', '1', '2022'], ['GAME001', 'BNMO - Play Along With Crypto', '100000', '3', '2020']], 3]
# print(buat_tabData('kepemilikan.csv'))
# [[['game_id', 'user_id'], ['GAME001', '1'], ['GAME002', '2'], ['GAME003', '2'], ['GAME001', '3'], ['GAME004', '1'], ['GAME005', '1']], 6]
