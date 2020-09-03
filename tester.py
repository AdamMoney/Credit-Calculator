import math
import sys

def test1():
    global diffcount
    list1 = ["--type=diff","--type=annuity"]
    difflist1 = ["tester.py","--type=annuity","--type=diff","--principal","--periods","--interest"]
    annlist1 = ["tester.py","--type=annuity","--payment","--periods","--interest"]
    diffcount = 0
    if sys.argv[1] not in list1:
        print("Incorrect parameters.")
    elif sys.argv[1] == "--type=diff":
            diffcount +=1
            for arg in sys.argv:
                if "--principal" in arg:
                    # print("PRINCIPAL")
                    diffcount +=1
                elif "--periods" in arg:
                    # print("PERIODS")
                    diffcount +=1
                elif "--interest" in arg:
                    diffcount +=1
                    # print("INTEREST")
                    # print (diffcount)
                elif "--payment" in arg:
                    # print("PAYMENT FOUND")
                    diffcount +=100
                    # print("Incorrect parameters")
                elif arg not in difflist1:
                    # print ("NOT IN DIFF LIST")
                    diffcount +=100
                    # print("Incorrect parameters")
    elif sys.argv[1] == "--type=annuity":
            diffcount +=1
            for arg in sys.argv:
                if "--payment" in arg:
                    # print("PAYMENT")
                    diffcount +=1
                elif "--periods" in arg:
                    # print("PERIODS")
                    diffcount +=1
                elif "--interest" in arg:
                    diffcount +=1
                    # print("INTEREST")
                    # print (diffcount)
                elif "--principal" in arg:
                    # print("PRINCIPAL FOUND")
                    diffcount +=1
                    # print("Incorrect parameters")
                elif arg not in difflist1:
                    # print ("NOT IN DIFF LIST")
                    diffcount +=100
                    # print("Incorrect parameters")
#
# print (sys.argv)
# print (sys.argv[1])


def goteverything():
    global diffcount
    if diffcount == 4:
        if sys.argv[1] == "--type=annuity":
            if "--payment" in sys.argv[2]:
                # print("ANNUI FOUND")
                separate1()
                # print ("GO ANNUITY")
                annuitystyle2()
            elif "--princ" in sys.argv[2]:
                if "--payment" in sys.argv[3]:
                    # print("ANNUI FOUND")
                    separate1()
                    # print ("GO ANNUITY")
                    annuitystlye3()
                elif "--periods" in sys.argv[3]:
                    # print("ANNUI FOUND")
                    separate1()
                    # print ("GO ANNUITY")
                    annuitystyle1()
        elif sys.argv[1] == "--type=diff":
            separate1()
            # print ("GO DIFF")
            diffstyle1()
    else:
        print("Incorrect parameters.")

def separate1():
    global principal
    global interest
    global payment
    global periods
    for arg in sys.argv:
        if "princ" in arg:
            PrincipalList = []
            for ch in arg:
                if ch.isnumeric():
                    PrincipalList.append(ch)
            separator = ""
            principal = separator.join(PrincipalList)
            principal = int(principal)
            # print ("Principal Found")
            # print (principal)
            # print (type(principal))
        if "periods" in arg:
            PeriodsList = []
            for ch in arg:
                if ch.isnumeric():
                    PeriodsList.append(ch)
            separator = ""
            periods = separator.join(PeriodsList)
            periods = int(periods)
            # print ("Periods Found")
            # print (periods)
            # print (type(periods))
        if "interest" in arg:
            interestList = []
            chars = set('0123456789.,')
            for ch in arg:
                if ch in chars:
                    interestList.append(ch)
            separator = ""
            interest = separator.join(interestList)
            interest = float(interest)
            # print ("Interest Found")
            # print (interest)
            # print (type(interest))
        if "payment" in arg:
            paymentList = []
            for ch in arg:
                if ch.isnumeric():
                    paymentList.append(ch)
            separator = ""
            payment = separator.join(paymentList)
            payment = int(payment)
            # print ("Payment Found")
            # print (payment)
            # print (type(payment))

def diffstyle1():
    # elif y == "d":
    # print("Enter the credit principal:")
    credit_principle = float(principal)
    # print("Enter the count of periods:")
    # periods = int(periods)
    # print("Enter the credit interest:")
    credit_interest = float(interest)
    i = float((credit_interest/12)/100)
    # print (i)
    month_count = periods
    start_month = 1
    overpayment = 0
    while start_month != month_count+1:
         #     get the first month payment correct to start with then work on the months whileloop
        stageone = credit_principle/periods
        # print(stageone)
        stagetwo = credit_principle-((credit_principle*(start_month-1))/periods)
        # print(stagetwo)
        stagethree = i*stagetwo
        # print(stagethree)
        stagefour = (math.ceil(stageone+stagethree))
        print (f"Month {start_month}: paid out {stagefour}")
        stagefive = stagefour-stageone
        # print (stagefive)
        overpayment += stagefive
        start_month += 1
    print("")
    print(f"Overpayment = {math.ceil(overpayment)}")



def annuitystyle1():
    # y == "a":
    # print("Enter the credit principal:")
    credit_principle = float(principal)
    # print("Enter the count of periods:")
    # periods = int(input())
    # print("Enter the credit interest:")
    credit_interest = interest
    i = float((credit_interest/12)/100)
    # print (i)
    stagethree = (i*(math.pow(1+i,periods)))/((math.pow(1+i,periods))-1)
    # print(stagethree)
    stagefour = float(math.ceil(credit_principle*stagethree))
    stagefive = int(stagefour)
    # print (round(stagefour,0))
    print("Your annuity payment = ",stagefive,"!",sep="")
    overpayment = int((stagefour*periods)-credit_principle)
    print ("Overpayment =", round(overpayment,0))

# elif y == "p": # happy - seems to work well long as int and floats are correct
def annuitystyle2():
    # print("Enter the monthly payment:")
    monthly_payment = payment
    # print("Enter the count of periods:")
    # periods = int(input())
    # print("Enter the credit interest:")
    credit_interest = interest
    i = float((credit_interest/12)/100)
    # print (i)
    stagethree = (i*(math.pow(1+i,periods)))/((math.pow(1+i,periods))-1)
    # print(stagethree)
    stagefour = int(monthly_payment/stagethree)
    # print (round(stagefour,0))
    print("Your credit principal = ",stagefour,"!",sep="")
    overpayment = int((monthly_payment*periods)-stagefour)
    print ("Overpayment =", round(overpayment,0))

def annuitystlye3():
    # print("Enter the credit principal:")
    # credit_principal = int(principal)
    # print(credit_principal)
    # print("Enter the monthly payment:")
    # monthly_payment = int(payment)
    # print (monthly_payment)
    # print("Enter the credit interest:")
    # credit_interest = float(interest)
    # print(credit_interest)
    i = float((interest/12)/100)
    # print(i)
    parttwo = (payment/(payment-(i*principal)))
    # print(parttwo)
    # print (type(parttwo))
    stagethree = math.log(parttwo,1+i)
    # print(stagethree)
    numbermonths = math.ceil(stagethree)
    # print(numbermonths)
    years = int(numbermonths/12)
    # print(years)
    months = int(numbermonths-(years*12))
    # print(months)
    if years > 1:
        if months > 1:
            print (f"You need {years} years and {months} months to repay this credit!")
        elif months == 1:
            print (f"You need {years} years and {months} month to repay this credit!")
        elif months == 0:
            print (f"You need {years} years to repay this credit!")
    elif years == 1:
        if months > 1:
            print (f"You need {years} year and {months} months to repay this credit!")
        elif months == 1:
            print (f"You need {years} year and {months} month to repay this credit!")
        elif months == 0:
            print (f"You need {years} year to repay this credit!")
    elif years == 0:
        if months > 1:
            print (f"You need {months} months to repay this credit!")
        elif months == 1:
            print (f"You need {months} month to repay this credit!")
    overpayment = int((payment*numbermonths)-principal)
    print ("Overpayment =", round(overpayment,0))


test1()
goteverything()




# print("What do you want to calculate?")
# print("""type "n" for the number of months,""")
# print("""type "a" for the annuity monthly payment,""")
# print("""type "p" for the credit principal: """)
# print("""type "d" for the differentiated payment: """)
#
# y = input()
# if y == "n":
#     print("Enter the credit principal:")
#     credit_principal = int(input())
#     print("Enter the monthly payment:")
#     monthly_payment = int(input())
#     print("Enter the credit interest:")
#     credit_interest = float(input())
#     i = float((credit_interest/12)/100)
#     # print(i)
#     stagetwo = (monthly_payment/(monthly_payment-i*credit_principal))
#     # print(stagetwo)
#     stagethree = math.log(stagetwo,1+i)
#     print(stagethree)
#     numbermonths = math.ceil(stagethree)
#     print(numbermonths)
#     years = int(numbermonths/12)
#     print(years)
#     months = int(numbermonths-(years*12))
#     print(months)
#     if years > 1:
#         if months > 1:
#             print (f"You need {years} years and {months} months to repay this credit!")
#         elif months == 1:
#             print (f"You need {years} years and {months} month to repay this credit!")
#         elif months == 0:
#             print (f"You need {years} year to repay this credit!")
#     elif years == 1:
#         if months > 1:
#             print (f"You need {years} year and {months} months to repay this credit!")
#         elif months == 1:
#             print (f"You need {years} year and {months} month to repay this credit!")
#         elif months == 0:
#             print (f"You need {years} year to repay this credit!")
#     elif years == 0:
#         if months > 1:
#             print (f"You need {months} months to repay this credit!")
#         elif months == 1:
#             print (f"You need {months} month to repay this credit!")
#
#
#     # n = math.log(1+nominal_rate)
#     # print (n)
#     # months = n*(monthly_payment/(monthly_payment-nominal_rate*credit_principal))
#     # print (months)
#
# elif y == "p": # happy - seems to work well long as int and floats are correct
#     print("Enter the monthly payment:")
#     monthly_payment = float(input())
#     print("Enter the count of periods:")
#     periods = int(input())
#     print("Enter the credit interest:")
#     credit_interest = float(input())
#     i = float((credit_interest/12)/100)
#     # print (i)
#     stagethree = (i*(math.pow(1+i,periods)))/((math.pow(1+i,periods))-1)
#     # print(stagethree)
#     stagefour = int(monthly_payment/stagethree)
#     # print (round(stagefour,0))
#     print("Your credit principal = ",stagefour,"!",sep="")
#
# elif y == "a":
#     print("Enter the credit principal:")
#     credit_principle = float(input())
#     print("Enter the count of periods:")
#     periods = int(input())
#     print("Enter the credit interest:")
#     credit_interest = float(input())
#     i = float((credit_interest/12)/100)
#     # print (i)
#     stagethree = (i*(math.pow(1+i,periods)))/((math.pow(1+i,periods))-1)
#     # print(stagethree)
#     stagefour = float(math.ceil(credit_principle*stagethree))
#     stagefive = int(stagefour)
#     # print (round(stagefour,0))
#     print("Your annuity payment = ",stagefive,"!",sep="")
#
# elif y == "d":
#     print("Enter the credit principal:")
#     credit_principle = float(input())
#     print("Enter the count of periods:")
#     periods = int(input())
#     print("Enter the credit interest:")
#     credit_interest = float(input())
#     i = float((credit_interest/12)/100)
#     print (i)
#     month_count = periods
#     start_month = 1
#     overpayment = 0
#     while start_month != month_count+1:
#          #     get the first month payment correct to start with then work on the months whileloop
#         stageone = credit_principle/periods
#         # print(stageone)
#         stagetwo = credit_principle-((credit_principle*(start_month-1))/10)
#         # print(stagetwo)
#         stagethree = i*stagetwo
#         # print(stagethree)
#         stagefour = (math.ceil(stageone+stagethree))
#         print (f"Month {start_month}: paid out {stagefour}")
#         stagefive = stagefour-stageone
#         # print (stagefive)
#         overpayment += stagefive
#         start_month += 1
#     print("")
#     print(f"Overpayment = {math.ceil(overpayment)}")
#
#
