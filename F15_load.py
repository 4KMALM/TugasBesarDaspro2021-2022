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

# ------- fungsi membuat list dari file -------
def buat_tabData(data):
    # Buat struktur ([list],Neff)
    sum_line = 0
    with open(data, 'r') as f:
        for line in f:
            sum_line += 1
    
    # sum_line-1 = 0 maka data kosong (hanya header)
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
