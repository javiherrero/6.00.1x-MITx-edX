# Desc: Problem Set 2 - Problem 1 - Paying the Minimum.
# Author: Javier Herrero Arnanz.

# Credit card details.
balance = 4842
totalPaid = 0
annualInterestRate  = 0.2
monthlyPaymentRate = 0.04
monthlyInterestRate = annualInterestRate/12.0

# For each month.
for month in range(1,13):
    # Compute the monthly payment.
    minPay = monthlyPaymentRate * balance
    
    # Update the outstanding balance.
    monUnpaidBalance = balance -minPay
    balance = (monUnpaidBalance * monthlyInterestRate) + monUnpaidBalance
    
    # Output the month, the minimum monthly payment and the remaining balance.
    print('Month: ' + str(month))
    print('Minimum monthly payment: ' + str(round(minPay,2)))
    print('Remaining balance: ' + str(round(balance,2)))
    
    # Keep track of the total amount of paid over all the past months so far.
    totalPaid += minPay
    
# Print out the result statement with the total amount paid and the remaining balance.
print('Total paid: ' + str(round(totalPaid,2)))
print('Remaining balance: ' + str(round(balance,2)))
