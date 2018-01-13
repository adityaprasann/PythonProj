# use map to create a function which finds the length of each word in the phrase (broken by spaces) and return the values in a list.
# the function will have an input of a string, and output a list of integers.
from functools import reduce
def word_lengths(phrase):
    return list(map(len, phrase.split()))

print(word_lengths('How long are the words in this phrase'))

# use reduce to take a list of digits and return the number that they correspond to. Do not convert the integers to strings
def digits_to_num(digits):
    return reduce(lambda x,y: x*10 + y, digits)
print(digits_to_num([3,4,3,2,1]))

# use filter to return the words from a list of words which start with a target letter.
def filter_words(word_list, letter):
    return list(filter(lambda x: x.startswith(letter), word_list))
l = ['hello','are','cat','dog','ham','hi','go','to','heart']
print(filter_words(l,'h'))

# use zip and list comprehension to return a list of the same length where each value is the two strings from L1 and L2 concatenated together with connector between them. Look at the example output below:
def concatenate(L1, L2, connector):
    return list( x + connector + y for x,y in zip(L1,L2))
print(concatenate(['A','B'],['a','b'],'-'))

# use enumerate and other skills to return a dictionary which has the values of the list as keys and the index as the value. You may assume that a value will only appear once in the given list.
def d_list(L):
    return { k : v for v,k in enumerate(L) }
print(d_list(['a','b','c']))

# use enumerate and other skills to return the count of the number of items in the list whose value equals its index.
def count_match_index(L):
    count = 0
    for item,idx in enumerate(L):
        if idx == item:
            count+=1
    return count
print(count_match_index([0,2,2,1,5,5,6,10]))