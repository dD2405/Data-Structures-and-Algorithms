def reverse_number(number):

    if(abs(number)>0xfffffff):
        return 0
    else:
        if(number>0):
            number=str(number)
            reverse=number[::-1]
        else:
            number=str(number)
            sign,number=number.split('-')
            print(sign)
            number=number[::-1]
            reverse='-'+number

    reverse=int(reverse)
    return reverse    

print(reverse_number(-114))
