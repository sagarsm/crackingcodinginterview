#Program to check if given array element can add upto given sum. You can use same element multiple times.
#Input: arr = [2, 3, 5, 7], sum = 10 Output: True
#Input: arr = [2, 3, 5, 7], sum = 1 Output: false
#this algorithm uses memoization to store the result of the subproblems to optimize the time complexity from o(n^m) to o(n * m))

arr = input("Enter array elements: ").split()

arr = [int(x) for x in arr]
#arr.sort()
sum = int(input("Enter sum: "))

def check_sum(arr, sum, memo = {}):
    if sum in memo:
        return memo[sum]
    if sum == 0:
        memo[sum] = True
        return True
    if sum < 0:
        return False
    for i in range(len(arr)):
        if check_sum(arr, sum - arr[i],memo):
            memo[sum] = True
            return True
    memo[sum] = False
    return False

print(check_sum(arr, sum))

#Input: arr = [2, 3, 5, 7], sum = 10 Output: [3 7]
#Input: arr = [2, 3, 5, 7], sum = 1 Output: []
#10:[2,2,2,2,2]

result = []
def how_sum(arr, sum):
    if (sum == 0):
        return []
    if (sum < 0):
        return None
    if sum < arr[0]:
        return None
    for i in arr:
        remainder = sum - i
        result = how_sum(arr, remainder)
        if result != None :
            result = result + [i]
            return result
    
    return None

print(how_sum(arr, sum))

def how_sum_memo(arr,sum, memo=None):
    if memo is None:
        memo = {}
    if sum in memo:
        return memo[sum]
    if sum == 0:
        return []
    if sum < 0:
        return None

    for i in arr:
        remainder = sum - i
        result = how_sum_memo(arr,remainder, memo)
        if result is not None:
            memo[sum] = result + [i]
            return memo[sum]

    memo[sum] = None
    return None

print(how_sum_memo(arr, sum))