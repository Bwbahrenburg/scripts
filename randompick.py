import random

itemlist = []
x =0

while x != 'q':
	x = input("Enter an item to list or type 'q' to exit \n")
	if x != 'q':
		itemlist.append(x)
	else:
		break
		
def Results():	
    results = random.choice(itemlist)
    print(f"\n You pick ", results)
    
Results()
again = input("\n Would you like another choice 'y' or 'n' ?  ")

while again == 'y':
	Results()
	again = input("\n Again 'y' or 'n'")

else:
	print("Thanks for playing")
