def longest(strings: list):
    longest = strings[0]
    for string in strings:
        if len(string) > len(longest):
            longest = string
    return longest