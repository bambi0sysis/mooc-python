def mean(l: list):
    Mean = sum(l) / len(l)
    return Mean

if __name__ == "__main__":
    my_list = [3, 6, -4]
    result = mean(my_list)
    print(result)