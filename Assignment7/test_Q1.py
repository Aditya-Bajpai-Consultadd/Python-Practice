from Ass7Q1 import is_prime  

def test_PrimeNumbers():
    assert is_prime(2) == True
    assert is_prime(3) == True
    assert is_prime(17) == True
    assert is_prime(19) == True

def test_NonPrimeNumbers():
    assert is_prime(0) == False  
    assert is_prime(1) == False  
    assert is_prime(4) == False
    assert is_prime(18) == False

def test_NegativeNumbers():
    assert is_prime(-1) == False  
    assert is_prime(-10) == False 
    assert is_prime(-17) == False 

def test_LargeNumbers():
    assert is_prime(7919) == True  
    assert is_prime(8000) == False  