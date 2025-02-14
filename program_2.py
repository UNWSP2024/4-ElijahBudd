# Program #2: Movie Tix
# Write a program that has the user input various movie names and how many
# tickets are desired for each movie.
# At the end of the program it prints out the total number of tickets desired by the user.
# Use either a "for loop" or "while loop" to accomplish this.

def main():

    ######################
    ticket_amount = 0

    while True:
        input("Enter movie name: ")
        ticket_amount += int(input("Enter amount of tickets: "))
        again = input("Do you need more tickets?(y or n): ")
        if again == "y":
            continue
        if again == "n":
            break
    print("You have:", ticket_amount, "tickets")
    ######################


if __name__ == '__main__':
    main()

Test Run:
Enter movie name: Star Wars
Enter amount of tickets: 3
Do you need more tickets?(y or n): y
Enter movie name: Minions
Enter amount of tickets: 2
Do you need more tickets?(y or n): n
You have: 5 tickets
