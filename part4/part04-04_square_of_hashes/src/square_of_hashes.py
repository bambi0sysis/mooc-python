def line(length: int, text: str):
    if text:
        print(text[0] * length)
    else:
        print("*" * length)

def square_of_hashes(size):
    i = size
    while i > 0:
        line(size, "#")
        i -= 1

if __name__ == "__main__":
    square_of_hashes(5)
