# Desc: Problem Set 2 - Problem 3 - Paying debt off in a year (Bisection Search).
# Author: Javier Herrero Arnanz.

# Credit card details.
balance = 999999
annualInterestRate  = 0.18
monthlyInterestRate = annualInterestRate/12.0

# Bisection search variables
lowBound =balance/12.0
upBound = (balance * ((1+monthlyInterestRate)**12))/12.0
threshold = 0.01

# Calculate the minimum fixed monthly payment.
payOffBalance = False
while (not payOffBalance):
    debt = balance
    monthlyPayment = (lowBound + upBound)/2.0
    
    # For each month.
    for month in range(1,13):    
        # Update the outstanding debt.
        monUnpaidBalance = debt - monthlyPayment
        debt = (monUnpaidBalance * monthlyInterestRate) + monUnpaidBalance
    
    # Is the debt paid?
    if ((debt >=0) and (debt <= threshold)):
        payOffBalance = True
    elif (debt > threshold):
        lowBound = monthlyPayment
    elif (debt < 0):
        upBound = monthlyPayment
        
    
# Print out the result statement with the lowest payment.
print('Lowest Payment: ' + str(round(monthlyPayment,2)))
