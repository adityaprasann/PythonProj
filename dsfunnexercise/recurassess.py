# write a recursive function which takes an integer and computes the cumulative sum of 0 to that integer For example, if n=4 , return 4+3+2+1+0, which is 10.

def rec_sum(n):
    sum = 0
    if n == 1:
        return 1
    sum = n + rec_sum(n-1)
    return sum
print(rec_sum(4))

# given an integer, create a function which returns the sum of all the individual digits in that integer. For example: if n = 4321, return 4+3+2+1
def sum_func(n):
    sum = 0
    divi = n//10
    rem = n%10
    if divi == 0:
        return rem
    sum = rem + sum_func(divi)
    return sum

print(sum_func(4321))

# create a function called word_split() which takes in a string phrase and a set list_of_words. The function will then determine if it is possible to split the string in a way in which words can be made from the list of words. You can assume the phrase will only contain words found in the dictionary if it is completely splittable.
def word_split(phrase, list_of_words, output = None):
    if output is None:
        output = []
    for word in list_of_words:
        if phrase.startswith(word):
            output.append(word)
            return word_split(phrase[len(word):],list_of_words,output)
    return output

print(word_split('themanran',['the','ran','man']))
print(word_split('ilovedogsJohn',['i','am','a','dogs','lover','love','John']))
print(word_split('themanran',['clown','ran','man']))

def reverse(s):
    if len(s) <= 1:
        return s
    return reverse(s[1:]) + s[0]

print(reverse('dlrow olleh'))

def permute(s):
    out = []
    if len(s) == 1:
        out.append(s)
    for idx,letter in enumerate(s):
        for perm in permute(s[:idx] + s[idx+1:]):
            out.append(letter + perm)
    return out

print(permute('abc'))


def fib_rec(n):
    if n == 1 or n == 2:
        return 1
    return fib_rec(n-1) + fib_rec(n-2)

print (fib_rec(10))
print (fib_rec(1))
print (fib_rec(23))

def fib_dyn(n):
    cache = {1:1,2:1}
    if(cache.get(n) != None):
        return cache.get(n)
    else:
        cache[n] = fib_dyn(n-1) + fib_dyn(n-2)
    return cache[n]

print (fib_dyn(10))
print (fib_dyn(1))
print (fib_dyn(23))

def fib_iter(n):
    a = 0
    b = 1
    for i in range(n):
        a, b = b, a + b
    return a

print (fib_iter(10))
print (fib_iter(1))
print (fib_iter(23))


