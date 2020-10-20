import time #this is here because I struggled with writing an efficient algorithm to compute the LCM for many numbers.
start_time = time.time() #first tries had a runtime of 45+ seconds lol.  This is down to about a second per number inputted until there are more than 10 inputs.

print("This program computes the Least Common Multiple (LCM) of how ever many integers of your choosing.\n")

number_list = [] #initializes list of user's inputted numbers
common_multiples = [] #initializes list of shared multiples
worst_case_scenario = 1 #initializes worst case scenario that LCM is all inputted numbers multiplied

try: #in case a string, negative or float is entered.
    total_numbers = int(input("How many numbers would you care to compute the LCM of?  "))
    if int(total_numbers) < 1: #in case zero is inputted
        print("Only positive integers can be entered here.  Please try again.")
    else:
        for k in range(1, total_numbers + 1): #creates list of user's inputted numbers
            number_k = int(input("Please input number " + str(k) + " of " + str(total_numbers) + ":  "))
            number_list.append(number_k)

        for number in number_list: #multiplies all of the user's numbers
            worst_case_scenario = worst_case_scenario * number

        for i in range(1, worst_case_scenario + 1): #tests all numbers in range to see if all numbers user inputted divide them
            if all(i % number == 0 for number in number_list):
                common_multiples.append(i)

        print(min(common_multiples)) #prints LCM

        print("--- %s seconds ---" % (time.time() - start_time)) #prints runtime

except ValueError: #in case a string float or negative is entered
    print("Only non-zero integers can be entered in this program!  Please try again.")