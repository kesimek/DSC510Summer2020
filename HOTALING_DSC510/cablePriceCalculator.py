# Programming Assignment 2.1 
# Michael Hotlaing
# This programm will:  
#	1) Welcome the user
#	2) Retrieve the company name from the user
#	3) Retrieve the number of feet of fiber optic cable to be installed from the user
#	4) Calculate the installation cost of fiber optic cable by multiplying
#	   the total cost as the number of feet times $0.87.
#	5) Print a receipt for the user including 
#	   The Company Name
#	   The Number of Feet of fiber optic cable to be installed
#	   The Calculated Cost
#	   The Total Cost

# Defining a Gloabl Variable for the price of fiber in case it ever changes
fiberPrice = 0.87

# Introdution
print("Hello! Welcome to the Fiber Optic Price Calculator!")

# Asking the user which company they are from
# Convert the company name to a string in case it is something like "101" Cable Oompany
company = input("Which company are you from?: ")
print("Okay! You are from " + str(company) +". That's great to hear!" )

# Asking the user how many feet of cable they will need for their job
# There is no error handling here, so if a string is passed, it will break the program
fiberLength = float(input("How many feet of fiber optic cable is required?: "))
print("Great! You will need " + str(fiberLength) + " feet of fiber optic cable! That will cost you $" + str(fiberLength * fiberPrice))

# Some print statements to create some room between the chat and the reciept
print()
print()

# Printing the reciept
print("--" + company + " Cable Company--")
print("--Fiber Optic Receipt--")
print("-Feet of Cable: " + str(fiberLength) + "-")
print("-Price per Foot: $" + str(fiberPrice) + "-")
print("-Total Cost: $" + str(fiberLength * fiberPrice) + "-")