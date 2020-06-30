def rev(st):
    st = st.split()
    rev = st[::-1]
    print(rev)
    rev = ' '.join(rev)
    return rev

s = "  hello world!  "
print(rev(s))
