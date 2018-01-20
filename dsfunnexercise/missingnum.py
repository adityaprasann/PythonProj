# Consider an array of non-negative integers. A second array is formed by shuffling the elements of the first array and deleting a random element. Given these two arrays, find which element is missing in the second array.
# Here is an example input, the first array is shuffled and the number 5 is removed to construct the second array.
# Input: finder([1,2,3,4,5,6,7],[3,7,2,1,4,6])
# Output: 5 is the missing number
import collections

def finder(arr1, arr2):
    for num in arr1:
        if num not in arr2:
            return num

def finder2(arr1, arr2):
    d=collections.defaultdict(int)
    for num in arr2:
        d[num] += 1
    for num in arr1:
        if d[num] == 0:
            return num
        else:
            d[num] -= 1

arr1 = [1,2,3,4,5,6,7]
arr2 = [3,7,2,1,4,6]
print(finder(arr1,arr2))
print(finder2(arr1,arr2))

arr1 = [5,5,7,7]
arr2 = [5,7,7]
print(finder(arr1,arr2))
print(finder2(arr1,arr2))