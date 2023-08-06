# Make a Program that verifies if a typed letter is a vowel or consonant.

letter = str(input("Enter a letter: ")).upper()

if letter[0] == 'A' or letter[0] == 'E' or letter[0] == 'I' or letter[0] == 'O' or letter[0] == 'U':
    print("The typed letter is a vowel")
else:
    print("The typed letter is a consonant")
