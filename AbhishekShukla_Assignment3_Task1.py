# Program to calculate factorial of a number taken as input from user.


# Define a function factorial
# function definition
def factorial(number):

    factorial = 1 # initialize the factorial as the last value of any factorial is 1 in the end. 
    while number > 1: # run while loop till the number is greater than 1. 
        factorial *= number # we are going to multiply fact with input from user. ex. 5 = 5 * 1
        number -= 1  # reduce the number for each iteration - 5 - 1 = 4 , 4 -1 = 3 .. till number reaches 1

    
    return factorial # function returns the output . not printing but returning .. 


input = int(input("Enter the number to calculate factorial:  ")) # input from user and store in input var

res = factorial(input) # function call and take input as result to pass in function above 
print(f"factorial of {input} is {res} ") # print result


# End of program 












    





