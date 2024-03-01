import random
drinks=["vodka", "tequila", "gin","beer","wine","mezcal","rum","pisco","seltzer","sake","scotch","whiskey","cognac"]
try:
    name=input("What is your name\n")
    age=input("How old are you\n")
    age=int(age) # convert string to integer
    country=input("Where are you from\n")
except ValueError:
    print("Invalid age. Please enter a number")
else:
    if age < 0 or age > 140:
        print("You are not human go back to your cave weird being")
    elif age > 120:
        print("You are too old to play, please go back to your grave")
    elif age < 18:
        print("You are a minor. You can't play the awesome drinking game")
    elif country == ("USA" or country=="UAE") and age < 21:
        print("You are a minor, no drinks for you")
    else:
        print("You are an adult. You can play the awesome drinking game")
        print("Have some", random.choice(drinks),"and enjoy the game")
