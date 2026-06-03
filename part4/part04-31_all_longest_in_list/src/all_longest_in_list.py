# def all_the_longest(l: list):
#     length = 0
#     long_list = []
#     for string in l:
#         if len(string) > length:
#             length = len(string)
#     for string in l:
#         if len(string) == length:
#             long_list.append(string)
#     return long_list

def all_the_longest(l: list):
    long_list = []
    length = 0
    for string in l:
        if len(string) > length:
            length = len(string)
            long_list = [string]
        elif len(string) == length:
            long_list.append(string)
    return long_list

# def all_the_longest(l: list):
#     result = []
#     for string in l:
#         if result == [] or len(string) > len(result[0]):
#             result = [string]
#         elif len(string) == len(result[0]):
#             result.append(string)
#     return result

# all_the_longest(["samantha", "rachel", "bombica"])