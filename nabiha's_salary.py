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

    

    