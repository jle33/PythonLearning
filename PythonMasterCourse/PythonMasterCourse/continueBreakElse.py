
shoppingList = ["milk", "eggs", "spam", "rice"]
for item in shoppingList:
    if item == "spam":
        continue #ends current iteration and moves to the next
        #break #-exits the loop
    print("Buy {0}".format(item))

meal = ["egg", "bacon", "spam", "sausages"]

for item in meal:
    if item == 'spam':
        nasty_food_item = item #python allows you to do this but will error out if "spam" is not in the array
        break
else : #you can attach an else to a for loop. Will always be called unless a break is called before it.
    print("Yea i'll like that.")
if nasty_food_item:
    print("Blah I don't like spam")
