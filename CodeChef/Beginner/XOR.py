t = int(input())
for i in range(t):
  r = 0
  n = int(input())
  a = [int(s) for s in input().split()]
  b = []
  print(b)

  for j in a:
    for k in a:
      b.append(j+k)
  print(b)
  for z in range(len(b)):
    r = r^b[z]
  print(r) 
