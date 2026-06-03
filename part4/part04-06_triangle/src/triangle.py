def line(length: int, text: str):
    if text:
        print(text[0] * length)
    else:
        print("*" * length)

def triangle(size):
    i = 1
    while i <= size:
        line(i, "#")
        i += 1

if __name__ == "__main__":
    triangle(5)