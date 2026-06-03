def invert(dictionary: dict):
    copy = {}
    for k,v in dictionary.items():
        copy[k] = v
        # copy[v] = k
    dictionary.clear()
    for k,v in copy.items():
        dictionary[v] = k    
    # for k,v in copy.items():
    #     dictionary[k] = v
    
# for k in dictionary:
#     copy[k] = dictionary[k]
# for k in copy:
#     del dictionary[k]
# for k in copy:
#     dictionary[copy[k]] = k