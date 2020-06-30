t = int(input())
li = []
w = 1
p1sum=p2sum=lead=0
for i in range(t):
    p1,p2 = map(int,input().split())
    diff = abs(p1-p2)
    li.append(diff)

    p1sum += p1
    p2sum += p2

    if(diff>=lead and p1sum>=p2sum):
        w = 1
    if(diff>=lead and p1sum<p2sum):
        w = 2

    new_lead = diff
    if new_lead>lead:
        lead = new_lead
print(w,lead)
