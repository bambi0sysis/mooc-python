def anagrams(string1, string2):
    string1 = sorted(string1)
    string2 = sorted(string2)
    for i in string1:
        if i in string2:
            return True
        return False
if __name__ == "__main__":
    anagrams("tame", "meta")