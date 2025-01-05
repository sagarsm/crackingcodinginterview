#Given a tring check if it is permutation of a palindrome

str=input("Enter a string: ")

def is_palindrome_permutation(str):
    str=str.lower()
    str=str.replace(" ","")
    dict={}
    for i in str:
        if i in dict:
            dict[i]+=1
        else:
            dict[i]=1
    odd_count=0
    for i in dict:
        if dict[i]%2!=0:
            odd_count+=1
    if odd_count>1:
        return False
    return True

print(is_palindrome_permutation(str))

