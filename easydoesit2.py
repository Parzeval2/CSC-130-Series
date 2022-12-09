
################################################################################
# Name: Julia Wilson
# Date: 10/3/2022
# Description: Easy Does It - Reloaded
################################################################################

# A function that prompts the user for a name and returns it to the
# calling statement.
def name():
    return input("Please enter your name: ")

# A function that prompts the user for a score and returns it to the
# calling statement.
def score():
    score1 = int(input("Enter your score: "))
    return (score1)
    

# A function that receives two numbers and returns the average of those
# two values to the calling statement.
def avg(score1,score2):
    average = int((score1+score2)/2)
    return average

# A function that receives a string and a number (the name and the
# average score) and prints it out on the screen in the appropriate format.
def sentence(a,b):
    print ("Hi, {}. Your average score is {}.".format(a,b))

#############################################################################
#       MAIN PART OF PROGRAM
# Functions that were defined above should be executed below in an order
# that satisfies the problem statement. Additional statements can be
# included below as well if needed.
#############################################################################

# prompt for name
z = name()
# prompt for two scores
x = score()
y = score()
# calculate the average
f = avg(x,y)
# display the final output
sentence(z,f)