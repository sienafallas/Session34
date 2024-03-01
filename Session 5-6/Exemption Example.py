name=input("What is your name\n")
age=input("How old are you\n")
try:
    age = int(age)  # convert string to integer
    birth_year = 2023 - age
    print("You were born in ", birth_year, ".", sep="")
    number=input("give me a number to divide the age\n")
    number=int(number)
    print(age / number)
except ValueError:
    print("Invalid age. Please enter a number")
except ZeroDivisionError:
    print("You cannot divide by zero")
except:
    print("Some other error I did not forsee")
else:
    print("No exceptions were raised")
finally:
    print("byee")

