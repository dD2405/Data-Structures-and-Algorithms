c = 0
x = 2
for i in range(1,7):
    x = x+1
    for j in range(1,7):
        if i%j == 0:
            c = c+1
        else:
            c = 0
if j>5:
    print(x,j)
