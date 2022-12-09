##########################################################################################
# Name: Grant Cooper
# Date: 10/28/22
# Description: Search Comparison
##########################################################################################
import math

# a function that displays the table
def table(Min,Max,Inter):
    print(" {:<20} | {:<20} | {:<20} | {:<20} ".format("N", "Seq", "Bin", "Perf"))
    while (Max > Min):
        print(" {:<20} | {:<20} | {:<20} | {:<20} ".format(Max, Seq(Max), Bin(Max), Perf(Seq(Max), Bin(Max))))
        Max = int(Max-Inter)


# a function that calculates the average number of comparisons of a sequential search on a list of size n
# -input: the list size
# -output: the average number of comparisons
def Seq(size):
    size = int(size)
    size2 = size/2
    size2 = math.floor(size2)
    return size2

# a function that calculates the maximum number of comparisons of a binary search on a list of size n
# -input: the list size
# -output: the average number of comparisons
def Bin(size):
    size2 = math.log(size+1,2)
    size2 = math.ceil(size2)
    return size2
#Performance Tab
def Perf(seq,bin):
    perf = seq/bin
    perf = math.ceil(perf)
    return perf

###############################################
# MAIN PART OF THE PROGRAM
###############################################
# get user input for the minimum (make sure that it is >= 0)
def minfun():
    Min = int(input("Please Enter the Minimum Value:"))
    if Min<0:
        print("ERROR: Minimum must be >= 0!")
        minfun()
    return Min

# get user input for the maximum (make sure that is is >= minimum)
def maxfun(Min):
    Max = int(input("Please Enter the Maximum Value"))
    if (Max<Min):
        print("ERROR: Maximum must be >= minimum" + Min + "!")

# get user input for the interval (make sure that it is >= 1)
Inter = int(input("Please Enter the Interval"))

# generate the table
min = minfun()
max = maxfun(min)

table(str(min), str(max), int(Inter))