name=input("What is your name\n")
age=input("How old are you\n")
#print("Hello,",name,"!")
print("Hello, " + name + "!")
age=int(age) # convert string to integer
birth_year = 2023 - age
print("You were born in ", birth_year, ".", sep="")
