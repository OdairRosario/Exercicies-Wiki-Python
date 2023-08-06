# Make a Program that asks what shift you study. Ask to type M-morning or A-afternoon or N- Night.
# Print the message "Good morning!", "Good afternoon!" or "Good night!" or "Invalid value!", as the case may be.

shift = str(input("What shift do you study\n Morning(M), Afternoon(A) or Night(N): "))

if shift[0].upper() == 'M':
    print("Good morning!")
elif shift[0].upper() == 'A':
    print("Good afternoon!")
elif shift[0].upper() == 'N':
    print("Good night")
else:
    print("Invalid entry")
