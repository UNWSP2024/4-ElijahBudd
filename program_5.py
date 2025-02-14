# Program #5: Bank Balance
# Write a program that asks the user to enter the amount that he or she has budgeted for a month.
# A loop should then prompt the user to enter each of his or her expenses for the
# month and keep a running total. (Enter 0 to exit the loop)
# When the loop finishes, the program should display the amount that the
# user is over or under budget.

def main():
    budget = 0.0
    difference = 0.0
    spent = 1.0         #initialize for while loop
    total = 0.0

    ######################
    budget = float(input("Enter your budget: "))
    while True:
        spent = float(input("Enter expenses cost (enter 0 to stop): "))
        if spent == 0.0:
            break
        total += spent
        continue
    difference = budget - total
    if difference > 0:
        print("You went under budget by", difference)
    if difference < 0:
        difference = difference * -1
        print("You went over budget by", difference)
    elif difference == 0:
        print("You went exactly on budget")
    ######################


if __name__ == '__main__':
    main()

Test Run:
Enter your budget: 20
Enter expenses cost (enter 0 to stop): 12.65
Enter expenses cost (enter 0 to stop): 3.45
Enter expenses cost (enter 0 to stop): 7.65
Enter expenses cost (enter 0 to stop): 0
You went over budget by 3.75
