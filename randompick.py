import random

itemlist = []
x=0

print("\n\n\n\n\n This program will randomly choose something out of a list you make. \n")

while x != 'q':
	x = input("\nEnter an item to list or type 'q' to exit \n")

	if x != 'q':
		if x  == '':
			print("\n\nYou need to enter something into the list\n")
			x = 0
		else:
			itemlist.append(x)
# Checking if choice is a duplicate
			if len(set(itemlist)) == len(itemlist):
				x=0
# Deletes duplicate if applicable
			else:
				print(f"\n\n {x} is already in the list enter another item\n\n")
				del itemlist[-1]
				x = 0
	else:
		break

# Random pick from list function
def Results():
	results = random.choice(itemlist)
	print(f"\n You pick *****  {results}  *****")

Results()

# Repeat the pick option
again = input("\n Would you like to make another choice 'y' or 'n' ? ")

while again == 'y':
	Results()
	again = input("\n Again 'y' or 'n' ")

else:
	print("\n\nThanks\n\n")

