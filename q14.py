def counter(lister):
    # ar = []
    # for i in lister:
    #     ar.append(len(i))
    # return ar
    # return [ar for ar in lister]
    return [*map(len, lister)]

li = ['cat', 'hod', 'lol', '']
print(counter(li))