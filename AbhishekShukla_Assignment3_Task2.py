# Program to take input from user and perform math functions

# start of program

# import math module - built in python module
import math 

# function to define sqrt / log / sin for a given input
def sqrt(num):

    sqrt = math.sqrt(num)
    return sqrt

def log(num):

    log = math.log(num)
    return log

def sin(num):

    sin = math.sin(num)
    return sin

# take user input

input = int(input("Enter a number"))

print(f"Square root: {sqrt(input)}")
print(f"logarithm: {log(input)}")
print(f"sine: {sin(input)}")