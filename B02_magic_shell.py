import time

def numGenerator(x) :
    a = 5897642
    c = 98076
    return ((a*x)+c)%5678

def kerang_ajaib() :
    permohonan = True
    seed = round(time.time()) 
    while permohonan :
        pertanyaan = input("silahkan bertanya pada kerang : ")
        randomized = (numGenerator(seed))
        n = randomized%10
        if type(pertanyaan) != None :
            if n == 0 :
                print("Tentu saja.")
            elif n == 1 :
                print("Iya.")
            elif n == 2 :
                print("Coba pikir sendiri.")
            elif n == 3 :
                print("Tidak.")
            elif n == 4 :
                print("Mungkin, tapi sepertinya tidak.")
            elif n == 5 :
                print("Mungkin, tapi sepertinya iya.")
            elif n == 6 :
                print("Pertanyaan aneh, tapi iya")
            elif n == 7 :
                print("Pertanyaan aneh, tapi tidak.")
            elif n == 8 :
                print("TIDAK TIDAK TIDAK.")
            elif n == 9 :
                print("Coba tanya lagi.")
        else :
            pass
        print("PUJA KERANG AJAIB!!!!!!")
        seed = round(time.time()) + n
        check = input("Apakah anda masih memerlukan petunjuk dari kerang (y/n) ? ").lower()
        if check == 'y' :
            print("===============================================================")
            print()
        elif check == 'n' :
            permohonan = False

kerang_ajaib()