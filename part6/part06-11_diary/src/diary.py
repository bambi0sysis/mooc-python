while True:
    print("1 - add an entry, 2 - read entries, 0 - quit")
    choice = int(input("Function: "))
    if choice == 0:
        print("Bye now!")
        break
    elif choice == 1:
        with open("diary.txt", "a") as f:
            f.write(input("Diary entry: ") + "\n")
            print("Diary saved\n")
    elif choice == 2:
        print("Entries:")
        with open("diary.txt", "r") as f:
            print(f.read())
