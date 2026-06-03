def line(length: int, text: str):
    if text:
        print(text[0] * length)
    else:
        print("*" * length)
        
def box_of_hashes(height):
    while height > 0:
        line(10, "#")
        height -= 1

if __name__ == "__main__":
    box_of_hashes(5)
