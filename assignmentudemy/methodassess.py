# write a function that computes the volume of a sphere given its radius.
def vol(rad):
    return (4.0/3) * 3.14 * rad**1

print (vol(3))

# write a function that checks whether a number is in a given range (Inclusive of high and low)

def ran_check(num,low,high):
    if(low <= num <= high):
        print('number in range')
    else:
        print('number not in range')

def ran_bool(num,low,high):
    if(low <= num <= high):
        return True
    else:
        return False

ran_check(3,1,10)
print(ran_bool(3,1,10))

# write a Python function that accepts a string and calculate the number of upper case letters and lower case letters.
st = 'Hello Mr. Rogers, how are you this fine Tuesday?'
def up_low(s):
    d={"upper":0, "lower":0}
    for char in s:
        if char.isupper():
            d["upper"]+=1
        elif char.islower():
            d["lower"]+=1
    print ("Original String : ", s)
    print ("No. of Upper case characters : ", d["upper"])
    print ("No. of Lower case Characters : ", d["lower"])

up_low(st)

# write a Python function that takes a list and returns a new list with unique elements of the first list.
def unique_list(l):
    return list(set(l))

sample_list = [1,1,1,1,2,2,3,3,3,3,4,5]
print(unique_list(sample_list))

# write a Python function to multiply all the numbers in a list.
def multiply(numbers):
    res = 1
    for num in numbers:
        res *= num
    return res

print(multiply([1,2,3,-4]))

# write a Python function that checks whether a passed string is palindrome or not.
def palindrome(s):
    return s == s[::-1]

print(palindrome('helleh'))

# write a Python function to check whether a string is pangram or not.
import string

def ispangram(st):
    cmpst = ''
    for char in st:
        if(char != ' '):
            cmpst = cmpst + char.lower()
    cmpst = ''.join(sorted(set(cmpst)))
    return cmpst == string.ascii_lowercase

print(ispangram('The quick brown fox jumps over the lazy dog'))

print(bin(1024))
print(hex(1024))
print(round(5.23222,2))

s = 'hello how are you Mary, are you feeling okay?'
if(s.lower() == s ):
    print(" is lower ")
else:
    print(" is not lower ")

s = 'twywywtwywbwhsjhwuwshshwuwwwjdjdid'
print(s.count('w'))

set1 = {2,3,1,5,6,8}
set2 = {3,1,7,5,6,8}
print(set1.difference(set2))
print(set1.union(set2))

print({x: x ** 3 for x in range(5)})

l = [1,2,3,4]
print(l.reverse())

l = [3,4,2,5,1]
print(l.sort())