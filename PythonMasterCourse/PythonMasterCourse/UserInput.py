name = input("Enter your name.")
age = int(input("Please enter your age {0}: " .format(name)))
if 18 <= age < 31:
   print("Welcome to club 18-30 holidays, {0}" .format(name))
else:
    print("Sorry, you are excluded as you are underage.")
