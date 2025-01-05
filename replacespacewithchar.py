#Given a string, replace all spaces with %20

str = input("Enter a string: ")
dict = {}
def replace_spaces(str):
    str = list(str)
    for (i, c) in enumerate(str):
        if str[i] == ' ':
            print(i)
            str[i] = '%20'
    return ''.join(str)

print(replace_spaces(str))
