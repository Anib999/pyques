def longer(lister):
    # return max(lister, key=len)
    a = ''
    for i in lister:
        if len(a) < len(i):
            a = i
    return a

li = ['cat', 'car', 'fear', 'center']

print(longer(li))