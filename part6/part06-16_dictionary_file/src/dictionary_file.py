with open('dictionary.txt') as file:
    content = {}
    for line in file:
        line = line.split(' - ')
        content[line[0]] = line[1]

with open('dictionary.txt', 'a') as file:
    while True:
        print('1 - Add word, 2 - Search, 3 - Quit')
        choice = int(input('Function: '))
        
        if choice == 1:
            finnish_word = input('The word in Finnish: ')
            english_word = input('The word in English: ')
            content[finnish_word] = english_word
            file.write(f'{finnish_word} - {english_word}\n')
            print('Dictionary entry added')

        elif choice == 2:
            search_term = input("Search term: ")
            for finnish_term, english_term in content.items():
                if search_term in finnish_term or search_term in english_term:
                    print(f'{finnish_term} - {english_term}')

        else:
            print('Bye!')
            break