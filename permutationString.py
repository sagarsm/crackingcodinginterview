#find if the string is permuation of the other string

str1 = input("Enter the first string: ")
str2 = input("Enter the second string: ")

def is_permutation(str1, str2):
    if len(str1) != len(str2):
        return False
    else:
        print(sorted(str1), sorted(str2))
        return sorted(str1) == sorted(str2) 
    
print(is_permutation(str1, str2))

def is_permutation_no_data_structure(str1, str2):
    if len(str1) != len(str2):
        return False
    else:
        char_count = {}
        for s in str1:
            if s in char_count:
                char_count[s] += 1
                print(char_count)
            else:
                char_count[s] = 1
        for s in str2:
            if s in char_count:
                char_count[s] -= 1
            else:
                return False
        return all(value == 0 for value in char_count.values())
    
print(is_permutation_no_data_structure(str1, str2))


    