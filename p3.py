###########################################################################################
# Name:
# Date:
# Description:
###########################################################################################

# function that prompts the user for a name and returns it
def username():
    x = input("Please input your name:")
    return x

# function that receives the user's name as a parameter, and prompts the user for an age and returns it
def userage(name):
    input("Hello," + str(name) + " what is your age?:")
    return
# function that receives the user's name and age as parameters and displays the final output
def userAgeName(username,userage):
    print("Hello" + str(username) + ", your age is " + str(userage) + ".")


###############################################
# MAIN PART OF THE PROGRAM
# implement the main part of your program below
# comments have been added to assist you
###############################################
# get the user's name
x = username()

# get the user's age
y = userage(x)

# display the final output
userAgeName(x,y)