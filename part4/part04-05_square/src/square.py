def line(length: int, text: str):
    if text:
        print(text[0] * length)
    else:
        print("*" * length)

def square(size, character):
    i = size
    while i > 0:
        line(size, character)
        i -= 1

if __name__ == "__main__":
    square(5, "x")