def read_fruits():
    with open('fruits.csv') as file:
        dic = {}
        for line in file:
            line = line.strip()
            l = line.split(';')
            # key = line.split(';')[0]
            # value = line.split(';')[1]
            dic[l[0]] = float(l[1])
    return dic