
def main():

    annual_salary = float(input("Enter your annual salary: "))
    portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))

    total_cost = float(input("Enter the cost of your dream home: "))
    semi_annual_raise = float(input("Enter the semi-annual raise, as a decimal: "))
    portion_down_payment = total_cost * 0.25
    current_savings = 0.0
    r = 0.04
    
    counter = 0

    while (current_savings < portion_down_payment):
            
        current_savings += current_savings*r/12
        current_savings += annual_salary / 12 * portion_saved
        counter += 1
        
        if ((counter % 6) == 0):
            annual_salary += semi_annual_raise*annual_salary



    print("Number of months: ", counter)

if __name__ == "__main__":
    main()
