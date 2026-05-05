# Day 3 - Treasure Island

print('''Welcome to Treasure Island.
Your mission is to find the treasure.''')

choice1 = input("You're at a cross road. Where do you want to go? Type 'left' or 'right': ").lower()

if choice1 == "left":
    choice2 = input("You come to a lake. Type 'wait' to wait for a boat. Type 'swim' to swim across: ").lower()
    if choice2 == "wait":
        choice3 = input("You arrive at three doors: one red, one yellow, and one blue. Which do you choose? ").lower()
        if choice3 == "yellow":
            print("You found the treasure. You win! 🏆")
        elif choice3 == "red":
            print("It's a room full of fire. Game over. 🔥")
        elif choice3 == "blue":
            print("You enter a room of beasts. Game over. 🐺")
        else:
            print("That door doesn't exist. Game over.")
    else:
        print("You were attacked by a trout. Game over. 🐟")
else:
    print("You fell into a hole. Game over. 🕳️")