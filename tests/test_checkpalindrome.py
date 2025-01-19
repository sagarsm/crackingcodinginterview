import sys
import os
from checkpalindrome import is_palindrome

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


def test_is_palindrome():
    assert is_palindrome('neveroddoreven') == True
    assert is_palindrome('racecar') == True
    assert is_palindrome('hello') == False
    assert is_palindrome('A man a plan a canal Panama'.replace(' ', '').lower()) == True
    assert is_palindrome('') == True
    assert is_palindrome('a') == True
    assert is_palindrome('ab') == False

def test_negative_is_palindrome():
    assert is_palindrome('') == True
    assert is_palindrome