###########################################################################################
# Name: 
# Date: 
# Description: 
###########################################################################################

# the algorithm implemented iteratively
def passSomeBeers(bottles):
	if (bottles > 0):
		if (bottles == 1):
			print("1 bottle of beer on the wall.")
			print("1 bottle of beer.")
			print("Take one down, pass it around.")
			print("No more bottles of beer on the wall.")
		elif (bottles == 2):
			print("2 bottles of beer on the wall.")
			print("2 bottles of beer.")
			print("Take one down, pass it around.")
			bottles = bottles - 1
			print("{} bottle of beer on the wall.".format(bottles))
			print()
			passSomeBeers(bottles)
		else:
			print("{} bottles of beer on the wall.".format(bottles))
			print("{} bottles of beer.".format(bottles))
			print("Take one down, pass it around.")
			bottles = bottles - 1
			print("{} bottles of beer on the wall.".format(bottles))
			print()
			passSomeBeers(bottles)


###############################################
# MAIN PART OF THE PROGRAM
###############################################
passSomeBeers(99)

