#print('Hello, World!')
#print(1 * 5)
#print(1 + 2)
#print('hello + ' + "world")
#greetings = "hi"
#myname = 'bond'
#print(greetings + " " + myname)
## My comment
#print('lala')
## Keyboard Input
#name = input("enter your name ")
#print(greetings + name)
#newspace = "hello\nbond"
#print(newspace)

# Visual Studio Commands
# Mass Comment Ctrl + K, Ctrl + C
# Mass Uncomment Ctrl + K, Ctrl + U
simpleNewSpace = """Hello
World"""
print(simpleNewSpace)

a = 12
b = 3

print(a + b)
print(a - b)
print(a * b)
print(a / b)    # Float
print(a // b)   # Integer, Whole Number
print(a % b)

for i in range(1, a//b): #Remember to use // for Integer or else the for loop won't work
    print(i)

print("End")

mystring = 'Blah'
print(mystring[3])
print(mystring[-4])
print(mystring[0:3])
print(mystring[0:])
print(mystring[:3])
print(mystring[0:4:2])  #Start:End:Step
print(mystring[::1])

age = 25
print("My age is " + str(age))
print("My age is {0} years" .format(age))

days = 28
print('''
January: {2}
February: {0}
March: {2}
April: {1}
May: {2}
June: {1}
July: {2}
August: {2}
September: {1}
October: {2}
November: {1}
December: {2}
''' .format(days, 5*6.50, '31'))

for i in range(1,12):
    print('Column 1 Number {0:2} Column 2 Squared {1:<10}' .format(i, i**2)) #{   : Alignment(< is left alignment, > is right alignment} For Integer

for i in range(1,2):
    print("Pi is approx. {0:.3}" .format(22/7)) #{   : Precision} For Decimel

for i in range(1, 12):
    print('No. {:<4} squared is {:<4} and cubed is {:<10}'.format(i, i ** 2, i ** 3)) 

