import argparse
import os

# ------- Prosedur load() -------
def load():
# Input : -
# output : sebuah path folder, dengan folder pasti berisi file yang akan digunakan
    parser = argparse.ArgumentParser()
    parser.add_argument("folder", type = str, nargs="?")
    args = parser.parse_args()

    if args.folder != None:
        for dirpath, dirnames, filenames in os.walk(os.getcwd()):
            for dir in dirnames:
                if dir == args.folder:
                    break

            if dir == args.folder:
                return os.path.join(dirpath,args.folder)
                break
        else:
            print(f"Folder \"{args.folder}\" tidak ditemukan.")
    else:
        print("Tidak ada nama folder yang diberikan!")

# cara penggunaan
# $ python F15-load.py nama_folder
# ouput; print(load())
# Disk:/..pathfolder../nama_folder
