def prime_numbers():
    n = 2
    while True:
        for i in range(2, n):
            if n % i == 0:
                break
        else:
            yield n
        n += 1
