
l = []
while True:
    print("The list is now", l)
    choice = input("a(d)d, (r)emove or e(x)it: ")
    if choice == "x":
        break
    elif choice == "d":
        l.append(len(l) + 1)
    elif choice == "r":
        if not l:
            continue
        l.pop()
    else:
        print("Invalid choice")
print("Bye!")


# l = []
# i = 1
# x = False
# counter = 0
# while True:
#     print("The list is now", l)
#     choice = input("a(d)d, (r)emove or e(x)it: ")
#     if choice == "x":
#         break
#     elif choice == "d":
#         if x or counter > 0:
#             # i -= (2 * counter)
#             x = False
#             counter = 0
#         l.append(i)
#     elif choice == "r":
#         if not l:
#             continue
#         l.pop(-1)
#         x = True
#         counter += 1
#     else:
#         print("Invalid choice")
#     i += 1 - (2 * counter)
# print("Bye!")