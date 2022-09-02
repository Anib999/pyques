def countNum(num):
    if num.count(5) >= 3 and num.count(11) == 2:
        return True
    else:
        return False

num = [1,2,3,4,5,5,5, 11, 11]
print(countNum(num))
