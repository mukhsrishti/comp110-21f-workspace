"""Finding duplicate letters in a word."""

__author__ = "730402368"

word: str = input("Enter a word: ")

i: int = 0
while i < len(word)-1:
    j: int = i+1
    while j< len(word):
        if word[i].lower() == word[j].lower():
            print("Found duplicate: True ")
        else:
            print("Found duplicate: False")

    #while j < len(word):
        #print(word[j])
    #i += 1 :