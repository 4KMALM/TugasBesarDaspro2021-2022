from primitif_function import *

def exit(x):
    print("Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (y/n)")
    pil_exit = input()
    if pil_exit == "Y" or pil_exit == "y" :
        save() # Memanggil fungsi save
    elif pil_exit == "N" or pil_exit == "n":
        print("Program selesai dan tidak menyimpan data pada file.")
    else : #jika input != Y, y, n, atau N
        exit(x)
    return

exit(x)

