def sum_of_positives(lst: list):
    sum = 0
    for i in lst:
        if i > 0:
            sum += i
    return sum
if __name__ == "__main__":
    print(sum_of_positives([1, -2, 3, -4, 5]))