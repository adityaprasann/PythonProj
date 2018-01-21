# Given a string,determine if it is compreised of all unique characters. For example, the string 'abcde' has all unique characters and should return True. The string 'aabcde' contains duplicate characters and should return false.

def uni_char(s):
    se = set(s)
    if len(s) == len(se):
        return True
    return False

def uni_char2(s):
    countlst = []
    for char in s:
        if char not in countlst:
            countlst.append(char)
        else:
            return False
    return True

print(uni_char('goo'))
print(uni_char('abcdefg'))

print(uni_char2('goo'))
print(uni_char2('abcdefg'))