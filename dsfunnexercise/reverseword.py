# Given a string of words, reverse all the words. For example: Given: 'This is the best' Return: 'best the is This'

def rev_word(s):
    revstr = ''
    splitlst = s.split()
    idx = len(splitlst) - 1
    while idx >= 0:
        revstr = revstr + splitlst[idx] + ' '
        idx -= 1
    return revstr


def rev_word1(s):
    return " ".join(reversed(s.split()))


def rev_word2(s):
    return " ".join(s.split()[::-1])


print(rev_word('Hi John,   are you ready to go?'))
print(rev_word('    space before'))

print(rev_word1('Hi John,   are you ready to go?'))
print(rev_word1('    space before'))

print(rev_word2('Hi John,   are you ready to go?'))
print(rev_word2('    space before'))
