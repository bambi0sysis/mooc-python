# def dict_of_numbers():
#     d = {}
#     l1 = ['zero','one','two','three','four','five','six','seven','eight','nine']
#     l2 = ['ten','eleven','twelve','thirteen','fourteen','fifteen','sixteen','seventeen','eighteen','nineteen']
#     l = ['twenty','thirty','forty','fifty','sixty','seventy','eighty','ninety']
#     # dic[0] = l1; dic[1] = l2
#     for i in range(len(l1)):
#         d[i] = l1[i]
#     for i in range(len(l2)):
#         d[10 + i] = l2[i]

#     for n in range(20, 100):
#         ones = n % 10
#         tens = n // 10
#         if tens < 3:
#             if ones == 0:
#                 d[n] = l[0]
#             else:
                
#                 d[n] = l[0] + "-" + l1[ones]
#         elif tens < 4:
#             if ones == 0:
#                 d[n] = l[1]
#             else:
#                 d[n] = l[1] + "-" + l1[ones]
#         elif tens < 5:
#             if ones == 0:
#                 d[n] = l[2]
#             else:
#                 d[n] = l[2] + "-" + l1[ones]
#         elif tens < 6:
#             if ones == 0:
#                 d[n] = l[3]
#             else:
#                 d[n] = l[3] + "-" + l1[ones]
#         elif tens < 7:
#             if ones == 0:
#                 d[n] = l[4]
#             else:
#                 d[n] = l[4] + "-" + l1[ones]
#         elif tens < 8:
#             if ones == 0:
#                 d[n] = l[5]
#             else:
#                 d[n] = l[5] + "-" + l1[ones]
#         elif tens < 9:
#             if ones == 0:
#                 d[n] = l[6]
#             else:
#                 d[n] = l[6] + "-" + l1[ones]
#         elif tens < 10:
#             if ones == 0:
#                 d[n] = l[7]
#             else:
#                 d[n] = l[7] + "-" + l1[ones]
#     return d


def dict_of_numbers():
    d = {}
    single = {0:"zero", 1:"one", 2:"two", 3:"three", 4:"four", 5:"five", 6:"six", 7:"seven", 8:"eight", 9:"nine"}
    doubles = {2: "twenty", 3: "thirty", 4: "forty", 5: "fifty", 6: "sixty", 7: "seventy", 8: "eighty", 9: "ninety"}

    for i in single:
        d[i] = single[i]

    d[10] = "ten"
    d[11] = "eleven"
    d[12] = "twelve"
    d[13] = "thirteen"
    d[14] = "fourteen"
    d[15] = "fifteen"
    d[16] = "sixteen"
    d[17] = "seventeen"
    d[18] = "eighteen"
    d[19] = "nineteen"

    for i in range(2, 10):
        d[i * 10] = doubles[i]
        for j in range(1, 10):
            d[i*10 + j] = doubles[i] + "-" + single[j]

    return d

if __name__ == "__main__":
    numbers = dict_of_numbers()
    print(numbers[2])
    print(numbers[11])
    print(numbers[45])
    print(numbers[99])
    print(numbers[0])