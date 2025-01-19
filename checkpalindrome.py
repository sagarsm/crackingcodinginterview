s = 'neveroddoreven'

def is_palindrome(s):
    return s == s[::-1]

if is_palindrome(s):
    print('Yes')
else:
    print('No')