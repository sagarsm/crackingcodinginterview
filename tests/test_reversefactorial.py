import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from reversefactorial import reverse_factorial

def test_reverse_factorial():
    assert reverse_factorial(2) == 2
    assert reverse_factorial(6) == 3
    assert reverse_factorial(24) == 4
    assert reverse_factorial(120) == 5
    assert reverse_factorial(720) == 6