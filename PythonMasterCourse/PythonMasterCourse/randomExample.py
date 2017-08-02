import random

highest = 10
answer = random.randint(1, highest)

print("Please guess a number between 1 and {}".format(highest))
guess = int(input())
dontStop = True

if answer == guess:
    dontStop = False

while dontStop:
    if guess == answer:
        print("Correct!")
        dontStop = False
    else:
        print("Guess Again!")
        if guess < answer:
            print("Guess Higher!")
        else:
            print("Guess Lower!")
        guess = int(input())
else:
    print("Oracle!!")