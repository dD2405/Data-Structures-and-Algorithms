def defangIP(string):

    result = string.replace('.' , '[.]')

    return result

print(defangIP('1.1.1.1'))
