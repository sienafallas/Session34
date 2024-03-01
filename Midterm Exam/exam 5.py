def palindrome(word):
    if word == word[::-1]:
        return True
    else:
        return False

# Check each number to see if it's a palindrome using the provided function
numbers = [
    "0974101607733149676776769413377061014790",
    "2704702208931031198668911301398022074072",
    "7798338247658278460338648728567428338977",
    "4257304920394478392772938744930294037524"
]

for number in numbers:
    if palindrome(number):
        print(f"{number} is a palindrome.")
    else:
        print(f"{number} is NOT a palindrome.")



