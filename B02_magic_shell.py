import time

def numGenerator(x) :
    # kamus lokal
    # x nilai pengali lcg
    # pengali
    # c inkremen
    # modulo
    a = 589764
    c = 98076
    m = 56784
    return ((a*x)+c)%m

def kerang_ajaib() :
    # seed untuk lcg awal didapat dari nilai round monotonic time
    # kemudian nilai randomized akan menjadi seed berikutnya
    # nilai randomized akan dimodulo 10 untuk menjadi parameter random kerang ajaib
    # kamus lokal 
    # seed : integer
    # n : integer
    # pertanyaan
    permohonan = True
    seed = round(time.monotonic()) 
    while permohonan :
        pertanyaan = input("silahkan bertanya pada kerang : ").lower()
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
                print("Pertanyaan aneh, tapi tidak.")
            elif n == 7 :
                print("Pertanyaan aneh, tapi iya.")
            elif n == 8 :
                print("TIDAK TIDAK TIDAK.")
            elif n == 9 :
                print("Coba tanya lagi.")
        else :
            pass
        print("PUJA KERANG AJAIB!!!!!!")
        seed = randomized
        check = input("Apakah anda masih memerlukan petunjuk dari kerang (y/n) ? ").lower()
        while check not in ['y','n'] :
            check = input("Kerang bilang \'ulangi lagi\' : ")
        if check == 'y' :
            print('===================================================')
        elif check == 'n' :
            print("Kerang bilang \"sampai jumpa\"") 
            permohonan = False
