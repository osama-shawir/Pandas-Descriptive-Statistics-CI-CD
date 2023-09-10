# -*- coding: utf-8 -*-

"""
TESTS goes here
"""


from main import IntFactorial

def test_main():
    print("The factorial of 4 is :", IntFactorial(4))
    assert IntFactorial(4) == 24

test_main()
