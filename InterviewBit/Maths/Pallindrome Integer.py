def isPalindrome(n):
    originalInteger = n
    reversedInteger=0
    while(n!=0):
        remainder = n%10;
        reversedInteger = reversedInteger*10 + remainder
        n /= 10;
        
    if(n>0):
        if(originalInteger==reversedInteger):
            return 1
        else:
            return 0

n = 123
print(isPalindrome(n))
