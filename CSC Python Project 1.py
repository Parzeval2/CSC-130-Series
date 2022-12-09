###########################################################################################
# Name:Grant Cooper
# Date: 9/26/2022
# Description: Script asks for name and age, then replies with name, age, and double age.
###########################################################################################

# prompt the user for a name and an age
name = input("What is your name? ")
age = int(input("How old are you, " + name +". "))
# display the final output
print("Hi " + name + "." " You are " + str(age) + " years old. Twice Your age is " + str(age*2))