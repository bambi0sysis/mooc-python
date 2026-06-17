def find_words(search_term: str):
    lst = []
    with open('words.txt') as file:
        for line in  file:
            lst.append(line.strip())
    result = []
    for word in lst:
        if search_term.startswith('*'):
            if word.endswith(search_term[1:]):
                result.append(word)
        elif search_term.endswith('*'):
            if word.startswith(search_term[:-1]):
                result.append(word)
        elif '.' in search_term:
            if len(search_term) == len(word):
                flag = True
                for ch in range(len(search_term)):
                    if search_term[ch] == '.':
                        continue
                    else:
                        if search_term[ch] == word[ch]:
                            flag = True
                        else:
                            flag = False
                            break
                if flag:
                    result.append(word)
        elif search_term == word:
            result.append(word)
    return result

