def binary(a,b):
    a_int,b_int = int(a,2),int(b,2)
    print(a_int,b_int)
    result = a_int + b_int

    return str(bin(result).replace('0b',''))

a,b = '100','11'

print(binary(a,b))
