def login(arrUser):
    username = input("Masukan username: ")
    password = input("Masukan password: ")

    # file selalau berisis judul
    pengguna = ['id','username','nama','password','role','saldo']   # Init

    for i in range(1, arrUser[1]):
        if arrUser[0][i][1] == username and arrUser[0][i][3] == password:
            pengguna = arrUser[0][i]
            break
    
    if pengguna == ['id','username','nama','password','role','saldo']:
        print("Password atau username salah atau tidak ditemukan.")
    else:
        print(f"Halo {pengguna[2]} Selamat datang di \"Binomo\".")
        return pengguna


# a = [[['id', 'username', 'nama', 'password', 'role', 'saldo'], ['1', 'fabian_si_banyak_fansnya00', 'Fabian Savero', 'yukmainbinomo', 'user', '100000'], ['2', 'akmal_ma', 'Akmal', 'akumaru', 'admin', '0'], ['3', 'username1', 'Zakariyya Gambetta', 'pass1', 'admin', '0'], ['4', 'username2', 'Margaretha Olivia', 'pass2', 'admin', '0'], ['5', 'username3', 'Kinanti Wening Asih', 'pass3', 'user', '10000000'], ['6', 'username4', 'Nadine Aliya Putri', 'pass4', 'user', '0']], 7]
# ---- Contoh valid -----
# >>> login(a)
# Masukan username: username2
# Masukan password: pass2
# Halo Margaretha Olivia Selamat datang di "Binomo".
# return -> ['4', 'username2', 'Margaretha Olivia', 'pass2', 'admin', '0']


