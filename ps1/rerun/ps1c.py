# -*- coding: utf-8 -*-
"""
Created on Tue Feb  9 12:03:49 2021

@author: a5020
"""

while True:
    try:
        starting_salary = float(input("Enter the starting salary:"))
        if(starting_salary <= 0):
            raise Exception
        break
    except ValueError:
        print("numbers please")
    except Exception:
        print("Integer for annual salary please")
        
        
semi_annual_raise = 0.07        
total_cost = 1000000
down_payment = total_cost * 0.25

epsilon = 100
step_counter = 1
low = 0
high = 10000
rate = ((high + low) // 2)/10000

def target_savings(salary, rate, semi_annual_raise):
    '''
    Calculates the total amount of savings given the salary, saving rate, and annual_raise of the person
    
    Parameters
    ----------
    salary : Integer
    rate : flaot
    semi_annual_raise : float

    Returns
    -------
    savings : float
    '''
    savings = 0
    for i in range (36):
        if (i != 0) and (i % 6 == 0):
            salary += salary*semi_annual_raise
        savings += ((savings*0.04)/12)
        savings += (salary/12)*rate
    return savings

if (target_savings(starting_salary, 1, semi_annual_raise) < down_payment):
        print("It is not possible to pay the down payment in three years")
else:
    savings = target_savings(starting_salary, rate, semi_annual_raise)
    while (abs(savings - down_payment) >= epsilon):
        if (savings > down_payment):
            high = (high + low) // 2
        else: 
            low = (high + low) // 2
        rate = ((high + low) // 2)/10000
        savings = target_savings(starting_salary, rate, semi_annual_raise)
        step_counter += 1
    print("Best savings rate:", rate)
    print("Steps in bisection search:", step_counter)
