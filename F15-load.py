import argparse
import os

# ------- Prosedur load() -------
def load():
    parser = argparse.ArgumentParser()
    parser.add_argument("folder", type = str)
    args = parser.parse_args()

    if args.folder != "":
        for dirpath, dirnames, filenames in os.walk(os.getcwd()):
            for dir in dirnames:
                if dir == args.folder:
                    break

            if dir == args.folder:
                return os.path.join(dirpath,args.folder)
                break

# cara penggunaan
# $ python F15-load.py nama_folder
# ouput; print(load())
# Disk:/..pathfolder../nama_folder
