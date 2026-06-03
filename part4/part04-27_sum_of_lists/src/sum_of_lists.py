def list_sum(l1: list, l2: list):
    l = []
    for i in range(len(l1)):
        l.append(l1[i] + l2[i])
    return l
if __name__ == "__main__":
    a = [1, 2, 3]
    b = [7, 8, 9]
    print(list_sum(a,b))

