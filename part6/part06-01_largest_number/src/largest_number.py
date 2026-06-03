def largest():
    large = 0 # this might cause errors with negative numbers
    with open('numbers.txt') as file:
        for line in file:
            line = int(line.strip())
            if line > large:
                large = line
        return large
            
def largest():
    with open("numbers.txt") as file:
        start = True
        biggest = 0
        for number in file:
            if start or int(number) > biggest:
                biggest = int(number)
                start = False
        return biggest