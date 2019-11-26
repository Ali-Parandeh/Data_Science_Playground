'''
Write function which takes string AAAAaaBCCCDDe as argument 
and returns its compressed version A4a2B1C3D2e1
'''

def compress(string):
    res = ''
    initial = string[0]
    res += string[0]
    count = 1
    for char in string[1:]:
        if char == initial:
            count += 1
        else:
            if count == 1:
                count = '1'
            res += str(count)
            count = 1
            initial = char
            res += char
    if (count >= 1):
        res += str(count)
    
    return res
    

print(compress("AAAAaaBCCCDDe"))
# A4a2B1C3D2e1