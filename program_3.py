# Program #3: Average Rainfall
# Write a program that uses nested loops to collect data and calculate the average
# rainfall over a period of years.
# The program should first ask for the number of years.
# The outer loop will iterate once for each year.
# The inner loop will iterate twelve times, once for each month.
# Each iteration of the inner loop will ask the user for inches of rainfall for each month.
# After all iterations, the program should display the number of months,
# the total inches of rainfall, and the average rainfall per month for the entire period.

def main():
    ######################
    number_of_years = int(input("Enter the number of years: "))
    number_of_months = number_of_years * 12
    total_rainfall = 0
    month = 1

    for o in range(number_of_years):
        for i in range(12):
            rainfall = float(input(f"Month {month}: Enter inches of rainfall: "))
            month += 1
            total_rainfall = total_rainfall + rainfall
    average_rainfall = total_rainfall / number_of_months

    print("Number of months:", number_of_months)
    print("Total rainfall:", total_rainfall)
    print(f"Average rainfall:  {average_rainfall:.2f}")
    ######################


if __name__ == '__main__':
    main()

Test Run:
Enter the number of years: 1
Month 1: Enter inches of rainfall: 13
Month 2: Enter inches of rainfall: 15
Month 3: Enter inches of rainfall: 17
Month 4: Enter inches of rainfall: 12
Month 5: Enter inches of rainfall: 7
Month 6: Enter inches of rainfall: 6
Month 7: Enter inches of rainfall: 14.7
Month 8: Enter inches of rainfall: 5.8
Month 9: Enter inches of rainfall: 18.93
Month 10: Enter inches of rainfall: 5
Month 11: Enter inches of rainfall: 13.65
Month 12: Enter inches of rainfall: 5
Number of months: 12
Total rainfall: 133.08
Average rainfall:  11.09
