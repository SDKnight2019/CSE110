favorite_letter = input("What is your favorite letter?") 

word = "supercalifragilisticexpialidocious"

for letter in word:
    if letter.lower() == favorite_letter.lower():
        print("_", end="")
    else:
        print(letter.lower(), end="")
