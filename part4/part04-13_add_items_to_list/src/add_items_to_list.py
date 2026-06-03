l = []
number = int(input("How many items: "))
i = 1
while i <= number:
    item = int(input(f"Item {i}: "))
    l.append(item)
    i += 1
print(l)