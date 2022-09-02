def test(lister, pref):
    ap = []
    for i in lister:
        if i.startswith(pref):
            ap.append(i)
    return ap

li = ['cat', 'dog', 'car']
pr = 'ca'
print(test(li, pr))

print(test(['post', 'lor', 'por'], 'po'))
