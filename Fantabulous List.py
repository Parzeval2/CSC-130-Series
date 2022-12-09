###########################################################################################
# Name: Grant Cooper
# Date: 10/31/2022
# Description:
###########################################################################################

# function that:
# (1) prompts the user for a list size
# (2) prompts the user for the integers to store in the list (corresponding to the list size)
# (3) creates the list
# (4) returns the list
def biglist():
    list = []
    length = int(input("How many integers would you like to add to the list?"))
    while(length>0):
        list.append(input("Enter an Integer:"))
        length -=1
    return list


###############################################
# MAIN PART OF THE PROGRAM
# implement the main part of your program below
# comments have been added to assist you
###############################################
# create the list
numbers = biglist()
# display information about the list using the list functions discussed in class
# there is no need to write/call your own functions here
print(numbers)
print(len(numbers))
print(min(numbers))
print(max(numbers))
numbers.reverse()
print(numbers)
numbers.reverse()
numbers.sort()
print(numbers)
