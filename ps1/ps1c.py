def savings_after_36(salary, rate):
    
    semi_annual_raise =  .07
    current_savings = 0.0
    r = 0.04
    
    for i in range (0,36):

        current_savings += current_savings*r/12
        current_savings += salary / 12 * rate

        if (((i+1) % 6) == 0):
            salary += semi_annual_raise*salary

    return current_savings


def main():

    salary = float(input("Enter the starting salary: "))

    total_cost = 1000000
    semi_annual_raise =  .07
    portion_down_payment = total_cost * 0.25
    current_savings = 0.0
    r = 0.04
    
    epsilon = 100
    counter = 0
    low = 0
    high = 100
    guess = round((high + low) / 2.0, 2)
    savs = savings_after_36(salary, (guess/100))

    if(savings_after_36(salary, 1) < portion_down_payment):
        print("It is not possible to pay the down payment in three years.")

    else:
        while (abs(savs - portion_down_payment) >= epsilon):
            if (savs < portion_down_payment):
                low = guess
            else:
                high = guess
            guess = round((high + low) / 2.0, 2)
            savs = savings_after_36(salary, (guess/100))
            counter += 1
        print("Best savings rate: ", (guess/100))
        print("steps in bisection search: ", counter)

if __name__ == "__main__":
    main()
