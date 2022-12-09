###########################################################################################
# Name: grant cooper
# Date: 11/8/2022
# Description:
###########################################################################################

# function that prompts the user for a list size, minimum and maximum values, creates the list, and returns it
# you must use the list functions discussed in class to add integers to the list
from random import randint
def numlist():
    size = int(input("How many integers would you like the list to have? "))
    min = int(input("What is the minimum value? "))
    max = int(input("What is the maximum value? "))
    count = 0
    numbers = []
    while (count<size):
        numbers.append(randint(min,max+1))
        count += 1
    return numbers
# function that receives the list as a parameter, and calculates and returns the mean
def mean(list):
    total = 0
    for i in list:
        total += i
    average = total/len(list)
    return average

# function that receives the list as a parameter, and calculates and returns the median
def median(list):
    mednum = len(list)/2
    return list[mednum]

# function that receives the list as a parameter, and calculates and returns the range
def range(list):
    list.sort()
    max = list[-1]
    min = list[0]
    range = max-min
    return range



###############################################
# MAIN PART OF THE PROGRAM
# implement the main part of your program below
# comments have been added to assist you
###############################################
# create the list
numbers = numlist()

# display the list
# there is no need to write/call your own function for this part
print(numbers)

# calculate and display the mean
print("The mean is " + str(mean(numbers)))

# calculate and display the median
print("The median is " + str(median(numbers)))

# calculate and display the range
print("The range is " + str(range(numbers)))