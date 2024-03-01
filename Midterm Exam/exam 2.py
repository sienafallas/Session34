import random

random_numbers = []

# Generate random numbers and append them to the list
for i in range(10):
    random_numbers.append(random.randint(1, 100))

# Replace numbers greater than 80 with their corresponding negative values
for i in range(len(random_numbers)):
    if random_numbers[i] > 80:
        random_numbers[i] = -random_numbers[i]

# Print the updated list
print(random_numbers)

# Create a list
my_list = [1, 2, 3, 4, 5]
# Change the second element of the list
my_list[1] = 10

# Print the updated list
print(my_list)

# Create a string
my_string = "hello"

# Try to change the second character of the string (which is 'e') to 'a'
# This will raise an error because strings are immutable
# my_string[1] = 'a'

# Instead, let's create a new string by concatenating parts of the original string
new_string = my_string[:1] + 'a' + my_string[2:]

# Print the new string
print(new_string)


