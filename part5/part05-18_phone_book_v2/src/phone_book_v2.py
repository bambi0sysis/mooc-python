def search(log: dict):
    name = input("name: ")
    if name not in log:
        print('no number')
    else:
        for value in log[name]:
            print(value)

def add(log: dict):
    name = input("name: ")
    number = input("number: ")
    if name not in log:
        # log[name] = [number]
        log[name] = []
    # else:
    #     log[name].append(number)
    log[name].append(number)

def main():
    log = {}
    while True:
        choice = input('command (1 search, 2 add, 3 quit): ')
        if choice == '1':
            search(log)
        elif choice == '2':
            add(log)
            print('ok!')
        else:
            break
    print('quitting...')

main()