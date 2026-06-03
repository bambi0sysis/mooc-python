# def shortest(l: list):
#     # length = 30
#     # apparently if the shortest is > 30?? so..
#     length = len(l[0])
#     for string in l:
#         if len(string) <= length:
#             length = len(string)
#             smallest = string
#     return smallest

# def shortest(l: list):
#     result = ""
#     for string in l:
#         if result == "" or len(string) < len(result):
#             result = string
#             # print(string)
#     return result

def shortest(l: list):
    if not l:
        return ""
    result = l[0]
    for string in l:
        if len(string) < len(result):
            result = string
            # print(string)
    return result

if __name__ == "__main__":
    my_list = ['Alan', 'Steve']
    result = shortest(my_list)
    print(result)