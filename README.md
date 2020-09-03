# CreditCalculator
 Credit Calculator designed to work from the terminal and return annuity or differentiated payment calculations. 

Example 1:
From the Terminal Type:

python creditcalc.py --type=diff --principal=1000000 --periods=10 --interest=10

This will return:

Month 1: payment is 108334
Month 2: payment is 107500
Month 3: payment is 106667
Month 4: payment is 105834
Month 5: payment is 105000
Month 6: payment is 104167
Month 7: payment is 103334
Month 8: payment is 102500
Month 9: payment is 101667
Month 10: payment is 100834

Overpayment = 45837

********************************************************************************************************************************

Example 2: finding the annuity payment for the 60-month (or 5-year) credit loan with the principal 1,000,000 and a 10% interest
From the Terminal Type:

python creditcalc.py --type=annuity --principal=1000000 --periods=60 --interest=10

This will return:

Your annuity payment = 21248!
Overpayment = 274880

********************************************************************************************************************************

Example 3: less than four arguments are given
From the Terminal Type:

> python creditcalc.py --type=diff --principal=1000000 --payment=104000

This will return "incorrect parameters" because at least three pieces of information are required to complete the calculations
out of the options "principal/payment/periods/interest":

Incorrect parameters.


********************************************************************************************************************************


Example 4: calculating differentiated payments given the principal 500,000, the period of 8 months, and an interest rate of 7.8%
From the Terminal Type:

python creditcalc.py --type=diff --principal=500000 --periods=8 --interest=7.8

This will return:

Month 1: payment is 65750
Month 2: payment is 65344
Month 3: payment is 64938
Month 4: payment is 64532
Month 5: payment is 64125
Month 6: payment is 63719
Month 7: payment is 63313
Month 8: payment is 62907

Overpayment = 14628



********************************************************************************************************************************



Example 5: calculating the principal for an individual paying 8,722 per month for 120 months (10 years) with an interest rate of 5.6%

From the Terminal Type:
python creditcalc.py --type=annuity --payment=8722 --periods=120 --interest=5.6

This will return:

Your credit principal = 800018!




********************************************************************************************************************************



Example 6: figuring out how much time an individual needs to repay the credit loan with the principal 500,000, the monthly payment of 23,000 at a 7.8% interest rate

From the Terminal Type:

python creditcalc.py --type=annuity --principal=500000 --payment=23000 --interest=7.8

This will return:

It will take 2 years to repay this credit!
Overpayment = 52000


