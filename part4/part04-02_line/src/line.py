def line(length: int, text: str):
    if text:
        print(text[0] * length)
    else:
        print("*" * length)
if __name__ == "__main__":
    line(5, "x")