
for i in range(1,20):
    print("i is now {}".format(i))

mystring = "abcdefghi"
for i in range(0, len(mystring)):
    if mystring[i] in 'aeh':
        #print(mystring[i]) #default end='\n' so we can change this to print(mystring[i],end=' ')
        print(mystring[i],end='')
print("\n")
for state in ["not pinin", "no more", "a stiff", "of life"]:
    print("This parrot is " + state)
    #or print("this parrot is {0}" .format(state))

for i in range(0, 100, 10):
    print("i is {0} ".format(i))

