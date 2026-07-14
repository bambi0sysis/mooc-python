from string import punctuation


def most_common_words(filename: str, lower_limit: int):
    freq = {}
    with open(filename) as file:
        for line in file:
            line = line.replace("\n", " ")
            for char in punctuation:
                line = line.replace(char, "")
            for word in line.split():
                if word:
                    freq[word] = freq.get(word, 0) + 1
    return {word: count for word, count in freq.items() if count >= lower_limit}
