listname = input('Enter list of number seperated by ,')
list = listname.split(',')
print(list)
print(tuple(list))

filename = input('Enter file name with extension')
fiEx = filename.split('.')
print(fiEx[-1])

namelist = ['Black', 'nile', 'ossan', 'chikuwa']
print(namelist[0], namelist[-1])