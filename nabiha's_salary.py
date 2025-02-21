def main():
    salary = float(input("Enter your salary for the month: "))
    month = input("Enter the month you are storing the salary for: ")
    saving = float(input("Enter the percentage for savings: "))
    rent = float(input("Enter the percentage for rent: "))
    electricity = float(input("Enter the percentage for electricity: "))
    
    savingA = (saving / 100) * salary
    rentA = (rent / 100) * salary
    electricityA = (electricity / 100) * salary
    total = savingA + rentA + electricityA
    remainder = salary - total
    Yrent = rentA * 12
    Yelectricity = electricityA *12
    newSalary = salary ** 2

    if savingA != 0:
        leftSaving = 50 / savingA
    else:
        leftSaving = 0
    
    print("\n Financial Summary for " + month)
    print("Salary: $" + str(round(salary, 2)))
    print("Savings: $" + str(round(savings_amount, 2)))
    print("Rent: $" + str(round(rent_amount, 2)))
    print("Electricity: $" + str(round(electricity_amount, 2)))
    print("Total Spent: $" + str(round(total_allocated, 2)))
    print("Money Left: $" + str(round(remainder, 2)))
    print("Yearly Rent: $" + str(round(yearly_rent, 2)))
    print("Yearly Electricity: $" + str(round(yearly_electricity, 2)))
    print("Salary Squared: " + str(round(salary_squared, 2)))
    print("Extra $50 divided by savings: " + str(round(savings_division, 2)))
    print("Savings left after $5 cut: $" + str(round(amount_left_in_savings, 2)) + "\n")


    

    