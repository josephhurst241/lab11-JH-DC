"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
import math


# First example
def add(a, b): 
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if b == 0:
        raise ZeroDivisionError("Divisor can't be zero")
    return a / b

def log(a,b):
    if b < 0 or a == 1 or a < 0:
        raise ValueError("Log argument and base can't be zero or below and log base can't be equal to 1")
    return math.log(a,b)

def exp(a, b):
    return a ** b









