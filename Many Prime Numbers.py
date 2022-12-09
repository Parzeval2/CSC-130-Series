#######################################################################
# author: Grant Cooper
# date: 12/2/2022
# desc:
########################################################################

# A function to prompt the user for a number and return that value to
# the calling statement.
def userprompt():
    x = input("What limit are you interested in?: ")
    return x
# A function that receives a number and tests that number to see whether
# it is prime or not. It returns the boolean response to the calling
# statement.
def primecheck(number):
    if number>1:
        for i in range(2, number):
            if number % i ==0:
                return False
            else:
                return True
        else:
            return False
        

################### MAIN ######################################
# Using the functions declared above, ask the user for a number, then
# create a list of all the prime numbers less than that number. Proceed
# to print out the relevant information related to that list.
primelist = []
userint = int(userprompt())
for i in range(2,userint):
    if primecheck(i) == True:
        primelist.append(i)
print("There are",str(len(primelist)),"prime numbers less than",str(userint))
print(primelist)