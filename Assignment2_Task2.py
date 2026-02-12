# sum of integers from 1 to 50 using for loop

# init a variable to store iteration of numbers

total = 0

# create a for loop to iterate from 1 to 51 , 51 will not be counted
for i in range (1,51):

    # for each iteration store total and sum it with numbers
    total += i # can also write this like - total = total + i

# print outside loop or else each iteration will be printed

print(f"The sum of numbers from 1 to 50 is : {total}")

# End of program