### picks an item from a user populated list
import random

itemlist = [] #starts with empty list
x=0
while x != 'q':
    x = input("Enter item to list or type 'q' to exit \n")
    if x != 'q':
        itemlist.append(x) #adds items to list unless 'q' is entered then it moves on
    else:
        break
    
#print (itemlist)
print("\n\n You pick ", random.choice(itemlist),"\n\n") #Randomly picks item from list and prints result
