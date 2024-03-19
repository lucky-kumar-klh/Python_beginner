import math
import random

print("\n****** Welcome to Random Number Guess Game !! ******")

print("\nCan you guess the Number in Minimum Attempts\n")

upper_bound = int(input("Enter Max Range: "))
lower_bound = int(input("Enter Min Range: "))

random_number = random.randint(lower_bound, upper_bound)
# print(f"Random Number: {random_number}")

minimum_tries = round(math.log2(upper_bound - lower_bound + 1))

print(f"You have been given {minimum_tries} Attempts\nGOOD LUCK !\n")
n_of_attempts = 0
while minimum_tries:
    
    user_number = int(input("\nGuess the Number: "))
    difference = abs(user_number - random_number)

    if user_number == random_number:
        print("Wow, What a guess\nYour Answer is Correct!")
        print(f"The Number was {random_number}")
        print(f"You guessed in your attempt no {n_of_attempts}\n")
        break
    else:
        if (user_number > random_number): 
            print(f"{user_number} is Greater than Random Number")
        else:
            print(f"{user_number} is Less than Random Number")

        print(f"{user_number} is Not the Answer, Try Again!")

    minimum_tries -= 1
    n_of_attempts += 1
    if minimum_tries == 0:
        print("OOPS!\nYou Lost the Game :((")
        print(f"The Answer was: {random_number}")
    print(f"{minimum_tries} Attempts Left !")
