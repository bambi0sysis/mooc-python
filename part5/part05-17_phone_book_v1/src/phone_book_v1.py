log = {}
while True:
    ask = int(input("command (1 search, 2 add, 3 quit): "))
    if ask == 1:
        name = input("name: ")
        if name not in log:
            print("no number")
        else:
            print(log[name])
    if ask == 2:
        name = input("name: ")
        number = input("number: ")
        log[name] = number
        print("ok!")
    elif ask == 3:
        print("quitting...")
        break