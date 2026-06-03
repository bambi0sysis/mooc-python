def same_chars(string: str, index1: int, index2: int):
    if index2 >= len(string) or index1 >= len(string):
        return False
    #return string[index1] == string[index2] or
    elif string[index1] == string[index2]:
        return True
    return False

if __name__ == "__main__":
    print(same_chars("coder", 1, 10))