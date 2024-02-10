max_score = int(input("Enter Maximum Score: "))
user_grade = int(input("Enter your Score: "))

if user_grade <= max_score and user_grade >= 0:
    if user_grade < max_score-(max_score*0.4):
        print("Your grade is F")
    elif user_grade < max_score-(max_score*0.3):
        print("Your grade is D")
    elif user_grade < max_score-(max_score*0.2):
        print("Your grade is C")
    elif user_grade < max_score-(max_score*0.1):
        print("Your grade is B")
    elif user_grade < max_score:
        print("Your grade is A")
    else:
        print("Your grade is A++")
else:
    print("Enter a Valid Score")
    