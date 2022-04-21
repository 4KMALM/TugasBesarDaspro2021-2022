import os

def save() :
    for tuple in os.walk("design code",topdown = True) :
        print(tuple)

save()
