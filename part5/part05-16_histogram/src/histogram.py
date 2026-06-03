def histogram(s: str):
    d = {}
    for ch in s:
        if ch not in d:
            d[ch] = "*" * 0
        d[ch] += "*"
    for key, value in d.items():
        print(key, value)

# histogram("statistically")