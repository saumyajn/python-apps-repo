print(
    r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
'''
)
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
name = input("What is your name? ")
print(f"Hello, {name.upper()}..")
print(
    "You just found a pirate's treasure map in an island nearby. "
    "Your mission is to find the treasure."
)
print(
    r"""
    *******************************************************************************
    ___
    ).x)
   (:_()

    *******************************************************************************
          """
)
print(
    "You're at a cross road. Where do you want to go? "
    "Type 'left' or 'straight' or 'right'"
)

direction = input("Enter your choice: ").lower()
if direction == "straight":
    print("You kept walking and looped back to the same position")
    print("Game OVER!")
elif direction == "right":
    print("Oops! You walked into the den of unknown. Game Over.")
elif direction == "left":
    print(
        "You've reached a pier. There is a boat to cross the river. "
        "Do you want to 'wait' for a boat or 'swim' across yourself?"
    )
    action = input("Enter your choice: ").lower()
    if action == "wait":
        print("You have crossed the river safely. ")
        print(
            "Now, you see 3 houses - one red, one yellow and one blue. "
            "Which colour do you choose?"
        )
        color = input("Enter your choice: ").lower()
        if color == "red":
            print("It's a room full of thorns and fire. 🔥 Game Over!")

        elif color == "blue":
            print("You enter a room of deadly robots. 🤖🔪 Game Over!")
        elif color == "yellow":
            print(
                f"Congratulations {name.upper()}!! You found the treasure! 🏆💰 You Win!"
            )
            print("You finally found the treasure chest filled with gold and jewels.")
        else:
            print("You chose a door that doesn't exist. Game Over!")
    else:
        print("AHHH!!! You are attacked by pirahnas. RIP! Game over!!")
else:
    print(f"You had 3 options, you have chosen none. So, Game over. ")
