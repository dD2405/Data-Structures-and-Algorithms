amt = int(input())
tot_amt = int(input())

if(amt%5==0):
    if(tot_amt>amt):
        tot_amt = tot_amt-amt-0.50
        print("%.2f" %tot_amt)
    else:
        print("%.2f" % tot_amt)
else:
    print("%.2f" % tot_amt)
    
