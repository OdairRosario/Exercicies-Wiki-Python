# Make a Program that checks if a typed letter is "F" or "M".
# According to the letter write: F - Female, M - Male, Invalid Sex.

sex = str(input("Enter your sex [M/F]: "))

if sex.upper() == 'M':
    print("Male")
elif sex.upper() == 'F':
    print("Female")
else:
    print("Invalid sex")
