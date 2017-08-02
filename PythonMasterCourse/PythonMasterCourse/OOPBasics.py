a = 12              #Each datatype is actually an object in python
b = 4
print(a + b)        # + calls the same function
print(a.__add__(b)) # __add__ is a method

class Kettle(object):

    powerSource = "Electricity" 

    def __init__(self, make, price): #Similar to a Constructor, is automatically called when a new object is stance of the class is created
        self.make = make #Member Variables - must use self.something
        self.price = price
        self.on = False

    def switch_on(self): #A method - different from a function is the presence of a self when defining a method. 
        self.on = True   #Self is the reference to the instance of the class i.e the "object instance of the class"

kenwood = Kettle("Kenwood", 9.99)
print(kenwood.make)
print(kenwood.price)

kenwood.price = 13.99
print(kenwood.price)

hamilton = Kettle("Hamilton", 12.99)
print(hamilton.make)
print(hamilton.price)

print("Models: {.make} = {.price}, {.make} = {.price}".format(kenwood, kenwood, hamilton, hamilton))

print(hamilton.on)
hamilton.switch_on()      #Knows that self is hamilton which is an instance of the Kettle Class
print(hamilton.on)

Kettle.switch_on(kenwood) #Alternate way to call switch_on(self) where self is a Kettle object
print(kenwood.on)

Kettle.powerSource = "None"
print(kenwood.powerSource)
print(hamilton.powerSource)
