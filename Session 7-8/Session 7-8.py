text = "abcdefjghijklmnop"
for letter in text:
    print(letter)

i=0
while i<len(text):
    print(text[len(text)-i-1], end="")
    i+=1


