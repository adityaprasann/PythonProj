#The method works as follows (see [here](https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes) for more details)
#1. Generate a list of all numbers between 2 and N
#2. Starting with $p=2$ (the first prime) mark all numbers of the form $np$ where $n>1$ and $np <= N$ to be not prime (they can't be prime since they are multiples of 2!)
#3. Find the smallest number greater than $p$ which is not marked and set that equal to $p$, then go back to step 2.  Stop if there is no unmarked number greater than $p$ and less than $N+1$

#`list_true` Make a list of true values of length $n+1$ where the first two values are false
def list_true(n):
    retl = [True] * (n+1)
    retl[0] = retl[1] = False
    return retl

# `mark_false` takes a list of booleans and a number $p$.  Mark all elements $2p,3p,...n$ false.
def mark_false(bool_list, p):
    count = 2
    while (count * p < len(bool_list)):
        bool_list[count * p] = False
        count = count + 1
    return bool_list

# `find_next` Find the smallest `True` element in a list which is greater than some $p$ (has index greater than $p$.
def find_next(bool_list, p):
    retVal = None
    for x in range(p+1, len(bool_list)):
        if(bool_list[x] and retVal == None):
            retVal = x
    return retVal

#`prime_from_list` Return indices of True values.
def prime_from_list(bool_list):
    retVal = []
    for ele,idx in enumerate(bool_list):
        if(idx):
            retVal.append(ele)
    return retVal

def sieve(n):
    bool_list = list_true(n)
    p = 2
    while p is not None:
        bool_list = mark_false(bool_list, p)
        p = find_next(bool_list, p)
    return prime_from_list(bool_list)

print(sieve(2000))

