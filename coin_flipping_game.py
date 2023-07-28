#Coin flipping game python code

import random
print("Welcome to the coin flipping game!")

choice = input("Enter your side (heads or tails): ")

num = random.randint(1,2)

if num == 1:
    result = "heads"

elif num == 2:
    result = "tails"

if choice == result:
    print("Good job! You won. The coin flipped ",result)

else:
    print("Aw... You lost. The coin flipped ", result)

print("Thanks for playing. Goodbye")
