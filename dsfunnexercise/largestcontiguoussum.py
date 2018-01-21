# Given an array of integers (positive and negative) find the largest continuous sum.

def large_cont_sum(arr):
    sum = 0
    idx = 0
    tempsum = 0
    while idx < len(arr):
        for num in arr[idx:len(arr)]:
            tempsum = tempsum + num
            sum = max(sum, tempsum)
        idx += 1
        tempsum = 0
    return sum


def large_cont_sum2(arr):
    if len(arr) == 0:
        return 0
    max_sum = current_sum = arr[0]
    for num in arr[1:]:
        current_sum = max(current_sum + num, num)
        max_sum = max(current_sum, max_sum)
    return max_sum


print(large_cont_sum([1, 2, -1, 3, 4, 10, 10, -10, -1]))
print(large_cont_sum([1, 2, -1, 3, 4, -1]))
print(large_cont_sum([-1, 1]))

print(large_cont_sum2([1, 2, -1, 3, 4, 10, 10, -10, -1]))
print(large_cont_sum2([1, 2, -1, 3, 4, -1]))
print(large_cont_sum2([-1, 1]))
