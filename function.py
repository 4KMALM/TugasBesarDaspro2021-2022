def check() :
    pass

# fungsi untuk parsing dengan pemisah char spasi
def pisah(string, pemisah) :
    x = []
    c = ""
    for i in string :
        if i != pemisah :
            c += i
        else :
            x += [c]
            c = ""
    x += [c]
    return x

# fungsi untuk memvalidasi kecocokan username password pada file
def validate(username,password,string) :
    pass

# fungsi untuk melakukan enkripsi pada password
def encrypt(password) :
    pass

# fungsi untuk melakukan dekripsi pada password
def decrypt(encrypted) :
    pass
    