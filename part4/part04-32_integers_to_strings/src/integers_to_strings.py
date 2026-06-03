def formatted(l: list):
    l2 = []
    for float in l:
        l2.append(f"{float:.2f}")
    return l2