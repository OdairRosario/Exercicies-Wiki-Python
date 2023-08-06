# Given the height (h) of a person as input data, construct an algorithm that calculates their ideal weight, using the following formulas:
# 1- For men: (72.7*h) - 58
# 2- For women: (62.1*h) - 44.7

height = float(input("Enter your height in cm: "))
height = height / 100

man = (72.7*height) - 58
woman = (62.1*height) - 44.7

print("\nIf you are a man, your ideal weight is:", man)
print("But if you are a woman, your ideal weight is:", woman)
