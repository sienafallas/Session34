text = "abcdefghijklmnop"
print(dir(text))
help(text.isupper)
print(text.isupper())
print("ABC".isupper())
print(text.upper())
print(text.upper().isupper())

new_text = text.upper()
print(text, new_text)
print("bannannanna". count("n"))
print("banabababnan". index("ana"))
print("banababanabnana".replace("ana","XXYYZZ"))
sentence = "Hello kind-sir; how many! I be of service today?"
punctuation = ".,;!?-"
for p in punctuation:
    sentence=sentence.replace(p, "")
print(sentence)

print("this is a sentence and I want the words".split(" "))

text= "Silje goes to mall. Silje likes shopping. I am friends with Silje. Such a nice girl Silje"
print(text.find("Silje"))
print(text.rfind("Silje"))

# Find all positions of Silje
i=0
while i <len(text):
    i = text.find("Silje", i)
    if i==-1:
        break
    print(i)
    i +=1
