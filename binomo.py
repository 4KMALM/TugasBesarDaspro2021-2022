import help
import function

print("Welcome to Binomo")
print("=======================")
print("Silahkan Login terlebih dahulu")
ingame = True
nama = input("Masukkan username : ")
password = input("Masukkan password : ")
login.login(nama,encrypt(password))
while ingame :
    print("Apa yang akan anda lakukan hari ini ? ")
    print("ketik \"help\" untuk petunjuk")
    todo = input()
    if todo == "help" :
       help.help(Role)