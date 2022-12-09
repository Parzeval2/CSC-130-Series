###########################################################################################
# Name: Grant
# Date: Cooper
# Description: Function recieves user input for name and age, outputs name, age,double age. Broken into 3 functions with
# 1 line calls to the functions.
###########################################################################################

# function that prompts the user for a name and returns it
def username():
    x = input("Please input your name:")
    return x

# function that receives the user's name as a parameter, and prompts the user for an age and returns it
def userage(name):
    x = input("Hello," + str(name) + " what is your age?:")
    return int(x)
# function that receives the user's name and age as parameters and displays the final output
def userAgeName(username, userage):
    print("Hello " + str(username) + ", your age is " + str(userage) + ". Double your age is ", str(userage*2))


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
userAgeName(x, y)
