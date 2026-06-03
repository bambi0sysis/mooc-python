# def anagrams(string1, string2):
#     string1 = sorted(string1)
#     string2 = sorted(string2)
#     if string1 == string2:
#         return True
#     return False
def anagrams(string1: str, string2: str):
    return sorted(string1) == sorted(string2)

if __name__ == "__main__":
    print(anagrams('house', 'mouse'))