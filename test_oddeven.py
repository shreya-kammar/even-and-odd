from evenodd import even

def test_even():
    assert even(10) == "Even number"

def test_odd():
    assert even(7) == "Odd number"

if __name__== "__main__":
    print("even and odd", even(33))