def greatest_number(a, b, c):
    if a > b and a > c:
        return a
    elif b > c:
        return b
    else:
        return c

if __name__ == "__main__":
    greatest = greatest_number(5, 8, 8)
    print(greatest)
#check equality too for safeness ig.
