l = []
while True:
    item = int(input("New item: "))
    if item == 0:
        break
    l.append(item)
    print("The list now:", l)
    print("The list in order:", sorted(l))
print("Bye!")