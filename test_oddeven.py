import sys 
from evenodd import even

def test_even():
    assert even(10) == "Even number"

def test_odd():
    assert even(7) == "Odd number"

if __name__== "__main__":
    num = int(sys.argv[1])