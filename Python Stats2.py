###########################################################################################
# Name: Grant Cooper
# Date: 10/12/2022
# Description:
###########################################################################################

# function that prompts the user to enter an integer and returns it
def getnumber():
    x = input("Please input a an integer:")
    return (x)

# function that receives three integers as parameters and returns the maximum of the three
def max(a,b,c):
    if (a>b):
        highest = a
    else:
        highest = b
    if (highest > c):
        return highest
    else:
        return (c)

# function that receives three integers as parameters and returns the minimum of the three
def min(a,b,c):
    if (a<b):
        lowest = a
    else:
        lowest = b
    if (lowest < c):
        return lowest
    else:
        return (c)

# function that receives three integers as parameters, and calculates and returns the mean
def mean(a,b,c):
    z = (a + b + c)
    p = (int(z) / 3)
    return (p)

# function that receives three integers as parameters, and calculates and returns the median
def median(a,b,c):
    if (max(a,b,c) != a and min(a,b,c) != a):
        return a
    if (max(a,b,c) != c and min(a,b,c) != c):
        return c
    if (max(a,b,c) != b and min(a,b,c) != b):
        return b

# function that receives three integers as parameters, and calculates and returns the mode
def mode(a,b,c):
    if (a == b or a == c):
        return a
    if (b == a or b == c):
        return b
    if (c == b or c == a):
        return c
    return ("Undefined")

# function that receives three integers as parameters, and calculates and returns the range
def range(a,b,c):
    x = max(a,b,c)
    y = min(a,b,c)
    z = x - y
    return z


###############################################
# MAIN PART OF THE PROGRAM
# implement the main part of your program below
# comments have been added to assist you
###############################################
# get three integers from the user
num1 = int(getnumber())
num2 = int(getnumber())
num3 = int(getnumber())

# determine and display the minimum value
print("The minimum is " + str(min(num1,num2,num3)))

# determine and display the maximum value
print("The maximum is " + str(max(num1,num2,num3)))

# calculate and display the mean
print("The mean is " + str(mean(num1,num2,num3)))

# calculate and display the median
print("The median is " + str(median(num1,num2,num3)))

# calculate and display the mode
print("The mode is " + str(mode(num1,num2,num3)))

# calculate and display the range
print("The range is " + str(range(num1,num2,num3)))