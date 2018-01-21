# Given a string in the form 'AAAABBBBCCCCCDDEEEE' compress it to become 'A4B4C5D2E4'. For this problem, you can falsely "compress" strings of single or double letters.

def compress(s):
    retstr = ''
    count = 1
    prevchar = ''
    for idx, char in enumerate(s):
        if idx == len(s) - 1:
            retstr = retstr + str(count + 1)
        if char == prevchar:
            count += 1
        else:
            if count == 1:
                retstr = retstr + char
            else:
                retstr = retstr + str(count) + char
                count = 1
        prevchar = char
    return retstr


print(compress('AAAAABBBBCCCC'))
print(compress('AABBCC'))
print(compress('AAABCCDDDDD'))
