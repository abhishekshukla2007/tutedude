# Number guessing game
import random
counter = 1
attempts = 10

correct_number = random.randint(1,50)
print(f"(DEBUG) Secret number is: {correct_number}")
print("Welcome to number guessing game you have 10 attemts to guess a number between 1 and 50, good luck !!")
while counter <= 10:
    print(f"You have {attempts} attempts left")
    guessed = int(input("Please enter the number you have guessed"))

    if guessed > 50:
        print("Enter number range 1 to 50")
    elif guessed == correct_number:
        print("Wow !! Congrats you have gussed the correct number- Game Over. Thanks for playing")
        break
    else:
        if guessed > correct_number:
            higher_lower = "Lower"
        else:
            higher_lower = "Higher"
        print(f"you'r guess is wrong try {higher_lower} number !!")    
     
    counter += 1
    attempts -=1

print(f"You have ran out of attempts - better luck next time.. psst the secret number was {correct_number}")