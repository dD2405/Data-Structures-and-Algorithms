t = int(input())

for i in range(t):

    s = str(input())

    c = s.count('1')

    if c%2 == 0:
        print('LOSE')
    else:
        print('WIN')
