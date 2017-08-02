i = 0
while i < 10:
    print("i is {}".format(i))
    i += 1

exits = ["east", "west", "north"]
choseExit = ""

while choseExit not in exits:
    choseExit = input("Enter a exit (east, west, north, south)")
    if choseExit == '':
        print("You have to do something.")
    elif choseExit == 'Quit':
        print("Game Over")
        break
else:
    print("you live")