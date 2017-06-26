for i in range(1, 12, 2): #range(start, end, step)
    if i >= 10:
        print("i >= 10")

    else:
        print("i < 10")

guess = int(input("Please enter a number between 1 and 5\n"))
if (guess <= 5):
    if guess == 5:
        print("Correct!")
    else:
        print("Try Again")
elif (guess > 5):
    print("Guess Lower")


name = input("Please enter your name: ")
age = int(input("Please enter your age, {0}: ".format(name)))
if (18 < age < 31):
    print("Welcome to the holiday club.") 
else:
    print("You are not welcome to the holiday club.")