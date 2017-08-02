#foo bar Control Flow practice
#If a number is divisable by 3 print foo
#If a number is divisable by 5 print bar
#If both print out foo bar
#Between number 1 & 20 incremented by 2 each time
for num in range(1,20,2):
    print(num)
    if num % 3 == 0 and num % 5 == 0:
        print("foo bar")
    elif num % 3 == 0:
        print("foo")
    elif num % 5 == 0:
        print("bar")

