inp = input('Enter a list of numbers using ,')
spIn = inp.split(',')


def checkin(inps):
    inputlength = len(inps)
    if inputlength > 4:
        checkfele = inps[4]
        print(checkfele)
        if inputlength == 8 and inps.count(checkfele) == 3:
            return True
        else:
            return False
    return False


print(checkin(spIn))
