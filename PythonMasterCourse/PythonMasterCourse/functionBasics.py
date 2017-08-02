#All parameters are pass by reference

def printme(str):
    print(str)

printme("Hi")

myArr = [1,2,3,4]
def addToArr(someArr):
    someArr.append(4)

print(myArr)
addToArr(myArr)
print(myArr)

def changeArr(someArr):
    someArr.append(["string", 2, 4, 3.3])

changeArr(myArr)
print(myArr)

def addIt(a,b):
    return 10 + 15

result = addIt(10, 15)
print(result)