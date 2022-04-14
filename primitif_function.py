def dataframe(x):
    total_data = 0
    with open(x, "r") as file:
        for line in file:
            total_data += 1
    return [[] for i in range(total_data)]


def data_constructor(x):
    list_data = []
    strings = ""
    delimiter = ";"
    nextline = "\n"

    with open(x, "r") as new_file:
        data = dataframe(x)
        data_counted = 0
        for line in new_file:
            for element in line:
                if element == delimiter or element == nextline:
                    list_data += [strings]
                    strings = ""
                else:
                    strings += element
            data[data_counted] = list_data
            list_data = []
            data_counted += 1
        return data


def length(x):
    count = 0
    for i in x:
        count += 1
    return count