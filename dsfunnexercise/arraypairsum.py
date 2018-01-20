# Given an integer array, output all the unique pairs that sum up to a specific value k.
# So the input: pair_sum([1,3,2,2],4)
# would return 2 pairs: (1,3) (2,2)

def pair_sum(arr,k):
    retlist = []
    for idx,num in enumerate(arr):
        diff = k - num
        if(diff in arr[idx:len(arr)]):
            retlist.append((num,diff))
    return retlist



print(pair_sum([1,3,2,2],4))