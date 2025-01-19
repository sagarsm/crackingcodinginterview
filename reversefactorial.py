X = int(input())
num =0

def calculatefactorial(num, memo={}):
    if num in memo:
        return memo[num]
    if num == 0 or num == 1:
        memo[num] = 1
        return 1
    elif num == 2:
        memo[num] = 2
        return 2
    else:
        memo[num] = num * calculatefactorial(num-1)
        return num * calculatefactorial(num-1)
    
for i in range(2,X+1):
    if X == calculatefactorial(i) :
        print(i)
        break 
