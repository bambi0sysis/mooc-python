def line(length: int, text: str):
    if text:
        print(text[0] * length)
    else:
        print("*" * length)

def shape(width: int, text: str, height: int, filler: str):
    i = 0
    while i < width:
        i += 1
        line(i, text)

    while height > 0:
        line(width, filler)
        height -= 1
    

if __name__ == "__main__":
    shape(5, "x", 2, "o")