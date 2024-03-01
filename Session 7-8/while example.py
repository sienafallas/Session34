import random
lives = 3
while lives > 0:
    print("You have", lives, "lives left.")
    # roll the dice
    dice = random.randint(1,6)
    print(" you rolled a", dice)
    # check if you win
    if dice == 6:
        print("\n\nYou win!\n\n")
        break
        lives -= 1
        
else:
    print("\n\nYou lose!\n\n")

print("Thank you for playing. Goodbye.")
