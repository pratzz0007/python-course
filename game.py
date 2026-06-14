import random

choices = ["snake", "water", "gun"]

computer = random.choice(choices)

user = input("Enter Snake, Water, or Gun: ").lower()

print("Computer chose:", computer)

if user not in choices:
    print("Invalid choice!")
elif user == computer:
    print("It's a tie!")
elif (user == "snake" and computer == "water") or \
     (user == "water" and computer == "gun") or \
     (user == "gun" and computer == "snake"):
    print("You win!")
else:
    print("Computer wins!")