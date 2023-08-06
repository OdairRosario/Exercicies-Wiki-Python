# João Fisherman, a good man, bought a microcomputer to control the daily yield of his work.
# Every time he brings a weight of fish greater than that established by the fishing regulations of the state of São Paulo (50 kilos) he must pay a fine of $4.00 per kilo excess.
# João needs you to make a program that reads the variable weight (fish weight) and calculates the excess.
# Record in the variable excess the amount of kilos beyond the limit and in the variable fine the amount of the fine that João will have to pay.
# Print the program data with the appropriate messages

fishWeight = float(input("What is the weight of the fish load?: "))

excess = fishWeight - 50

fine = excess * 4

print("\nJoão, you exceeded {}kg so you should pay a fine of ${}.".format(excess, fine))
