# Desc: Problem Set 2 - Problem 2 - Paying debt off in a year.
# Author: Javier Herrero Arnanz.

# Credit card details.
balance = 3926
annualInterestRate  = 0.2
monthlyInterestRate = annualInterestRate/12.0
minPayment = 10

# Calculate the minimum fixed monthly payment.
payOffBalance = False
monthlyPayment = minPayment
while (not payOffBalance):
    debt = balance
    
    # For each month.
    for month in range(1,13):    
        # Update the outstanding debt.
        monUnpaidBalance = debt - monthlyPayment
        debt = (monUnpaidBalance * monthlyInterestRate) + monUnpaidBalance
    
    # Is the debt paid?
    if (debt <= 0):
        payOffBalance = True
    else:
        monthlyPayment += minPayment
    
# Print out the result statement with the lowest payment.
print('Lowest Payment: ' + str(monthlyPayment))
