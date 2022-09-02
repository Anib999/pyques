inp = int(input('Enter stone number'))

def test(n):
    arr = []
    for i in range(n):
         arr.append(n+2 * i)
    return arr
    # return [n + 2 * i for i in range(n)]

print(test(inp))