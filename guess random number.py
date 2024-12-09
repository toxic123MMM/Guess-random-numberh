import random
playing=True
num=str(random.randint(0,10))
print("i will generate a random which you have to guess.")
print("Guess a number 0 to 10,Guess 1 digit at a time.")
print("The game will end when you guess the correct number")

while playing:
    guess=input("Give your best guess: ")
    if num == guess:
        print("You have won the match")
        print("the number was",num)
        break
    else:
        print("Your guess is incorrect try again")