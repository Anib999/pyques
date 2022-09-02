def finder(lister, con):
    return [s for s in lister if con in s]

li = ['cat', 'car', 'fear', 'center']
pr = 'ca'

a = ['cat', 'dog', 'shatter', 'donut', 'at', 'todo']
print(finder(li, pr))
print(finder(a, 'o'))