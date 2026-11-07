import random 
ROCK = 1 
PAPER = 2
SCISSORS = 3  
program_choice = random.randint(ROCK,SCISSORS)
user_choice = random.randint(ROCK,SCISSORS)

# we can combine nested conditions using and operator 
if user_choice == ROCK: 
    if program_choice == PAPER: 
        print("Program Won")
    elif program_choice == SCISSORS: 
        print("User Won") 
    else: 
        print("Tie")
elif user_choice == PAPER: 
    if program_choice == ROCK: 
        print("User Won")
    elif program_choice == SCISSORS: 
        print("Program Won")
    else: 
        print("Tie")
elif user_choice == SCISSORS: 
    if program_choice == ROCK: 
        print("Program Won")
    elif program_choice == PAPER: 
        print("User Won")
    else:
        print("Tie")