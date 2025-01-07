# Unique String: Implement an algorithm to determine if a string has all unique characters. 
# What if you cannot use additional data structures? check if a string has all unique characters

str = input("Enter a string: ")
print("The string is: ", str)

def is_unique(str):
    char_count = {}
    unique = True
    for s in str:
        if s in char_count:
            unique = False
            break
        char_count[s] = 1
    if unique:
        print(f'The string is unique \b {str}' )
    else:
        print(f'The string is not unique \b {str}')

def is_unique_no_data_structure(str):
    unique = True
    for i in range(len(str)):
        for j in range(i+1, len(str)):
            if str[i] == str[j]:
                unique = False
                break
    if unique:
        print(f'The string is unique \b {str}' )
    else:
        print(f'The string is not unique \b {str}')

def is_unique_bit_operator(str):
    checker = 0
    for s in str:
        val = ord(s) - ord('a')
        print(f'val {val}')
        if (checker & (1 << val)) > 0:
            return False
        checker |= (1 << val) 
        print(f'checker {checker}')
    return True

is_unique(str)
is_unique_no_data_structure(str)
print(is_unique_bit_operator(str))




    