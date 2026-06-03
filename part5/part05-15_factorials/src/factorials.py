def factorials(n: int):
    f = {}
    fact = 1
    for i in range(1, n + 1):
        fact *= i
        f[i] = fact
    return f
    
    # f = {}
    # f[1] = 1
    # for i in range(2, n + 1):
    #     f[i] = f[i - 1] * i
    return f