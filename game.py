# creater: OM DESHMUKH

# A simple example of snake water gun game

import random

def snake_water_gun():
    choices = ["snake", "gun", "water"]
    comp_choice = random.choice(choices)
    
    user_choice = input("Enter your choice (snake/gun/water): ").lower()
    
    if user_choice not in choices:
        print("Invalid choice. Please enter correct choice.")
        return
    
    print(f"Computer choice: {comp_choice}")
    
    if comp_choice == user_choice:
        print("It's a draw.")

    elif comp_choice == "snake" and user_choice == "water":
        print("Computer wins.")
    elif comp_choice == "gun" and user_choice == "snake":
        print("Computer wins.")
    elif comp_choice == "water" and user_choice == "gun":
        print("Computer wins.")
    else:
        print("user wins ")    

snake_water_gun()