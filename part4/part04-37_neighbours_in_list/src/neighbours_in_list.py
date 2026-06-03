def longest_series_of_neighbours(l: list):
    # l2 = []
    l1 = []
    count = 0
    for n in range(len(l) - 1):
        if l[n + 1] - l[n] == 1 or l[n] - l[n + 1] == 1:
            # l2.append(l[n])
            count += 1
        else:
            count = 0
        l1.append(count)
    return max(l1) + 1

# # gpt: 
# def longest_series_of_neighbours(l: list):
#     max_count = 0
#     count = 0

#     for a, b in zip(l, l[1:]):
#         if abs(a - b) == 1:
#             count += 1
#             if count > max_count:
#                 max_count = count
#         else:
#             count = 0

#     return max_count + 1 if l else 0

if __name__ == "__main__":
    my_list = [1, 2, 5, 7, 6, 5, 6, 3, 4, 1, 0]
    print(longest_series_of_neighbours(my_list))